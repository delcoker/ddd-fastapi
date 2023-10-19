import json
from typing import Dict, Any, List

import functional as fn
import pandas as pd
from loguru import logger

from config import BIRD_ISLAND_ID, GAZA_ID, WEST_BANK_ID
from src.domain.repositories.api.api_repository import ApiRepository
from src.domain.services.global_data_aggregation_service import GlobalDataAggregationService
from src.infrastructure.models.dto.api_result import ApiResult


class GlobalDataAggregationServiceImpl(GlobalDataAggregationService):

    def __init__(self,
                 global_geo_repository: ApiRepository,
                 centroid_repository: ApiRepository,
                 ):
        self.global_geo_repository = global_geo_repository
        self.centroid_repository = centroid_repository

    def get_global_data(self) -> Dict[str, Any]:
        geo_json = self.get_global_geo_data()
        centroid_df = self.get_centroid_data()  # TODO: pipe 1

        # TODO: use pipeline pattern -> PIPE 1
        geo_properties_list = (fn.seq(geo_json["features"])
                               .map(lambda feature: feature["properties"])
                               .to_list())
        geo_properties_df = pd.DataFrame(geo_properties_list)

        centroid_merged_df = geo_properties_df.merge(centroid_df[['adm0_code', 'longitude', 'latitude']],
                                                     left_on="adm0_id",
                                                     right_on="adm0_code",
                                                     how="left")

        centroid_features = (fn.seq(geo_json["features"])
                             .map(lambda feature: self.add_centroid_key(feature, centroid_merged_df))
                             .to_list())

        geo_json['features'] = centroid_features

        return geo_json

    def add_centroid_key(self, json_feature, centroid_merged_df: pd.DataFrame) -> Dict:
        adm0_id = json_feature["properties"]["adm0_id"]

        centroid_data_row = centroid_merged_df[centroid_merged_df["adm0_id"] == adm0_id]

        centroid_key = {
            'centroid': {'longitude': None, 'latitude': None}
        }

        if len(centroid_data_row) > 0:
            longitude = centroid_data_row['longitude'].values[0]
            latitude = centroid_data_row['latitude'].values[0]
            try:
                centroid_key = {
                    'centroid': {
                        'longitude': longitude if pd.notnull(longitude) else None,
                        'latitude': latitude if pd.notnull(latitude) else None,
                    }
                }
            except Exception as e:
                logger.error(f'country centroid with ADMIN 0 ID: {adm0_id} retrieval failure')
                logger.error(str(e))

        json_feature["properties"].update(centroid_key)
        return json_feature

    def get_global_geo_data(self) -> Dict:  # -> json:  # admin 0 level data
        api_result: ApiResult = self.global_geo_repository.fetch_data()
        if api_result.is_successful:
            geo_json = api_result.response_data.json()

            self.update_venezuela_and_palestine(geo_json)

            return geo_json
        else:
            logger.error(f'global geo data retrieval was unsuccessful. Error: {api_result.error}')
            pass  # TODO should app crash if it can't retrieve GEO data because merges can't continue

    def get_centroid_data(self) -> pd.DataFrame:
        centroid_result = self.centroid_repository.fetch_data()

        if centroid_result.is_successful:
            data = centroid_result.response_data.json()
            return pd.DataFrame(data)
        else:
            logger.error(f'centroid data retrieval was unsuccessful.'
                         f'Error: HTTP error {centroid_result.response_data.status_code} {centroid_result.error}')
            # TODO: replace with actual centroid result from api/db call
            return pd.read_json('dummy_centroids_adm0.json')
            # raw_centroid_df = pd.read_csv('dummy_centroids_adm0.csv')
            # columns_to_check = ["adm0_code", "longitude", "latitude"]
            # mask = raw_centroid_df[columns_to_check].map(lambda x: str(x).replace('.', '').isnumeric()).all(axis=1)
            # raw_centroid_df = raw_centroid_df[mask]
            # centroid_df = raw_centroid_df.astype({"Id": int, "adm0_code": int, "longitude": float, "latitude": float})
            # return centroid_df
            # TODO END: delete from above TODO

    # TODO write test for merged data
    # TODO moved logic to merged_split_countries_service
    def update_venezuela_and_palestine(self, geo_json) -> None:
        exclude_ids = [BIRD_ISLAND_ID, GAZA_ID, WEST_BANK_ID]
        geo_properties_list = (fn.seq(geo_json["features"])
                               .filter(lambda prop: prop["properties"]['adm0_id'] not in exclude_ids)
                               .to_list())

        bird_island = (fn.seq(geo_json["features"])
                       .filter(lambda prop: prop["properties"]['adm0_id'] == BIRD_ISLAND_ID)
                       .to_list())

        gaza = (fn.seq(geo_json["features"])
                .filter(lambda prop: prop["properties"]['adm0_id'] == GAZA_ID)
                .to_list())

        west_bank = (fn.seq(geo_json["features"])
                     .filter(lambda prop: prop["properties"]['adm0_id'] == WEST_BANK_ID)
                     .to_list())

        geo_json['features'] = geo_properties_list

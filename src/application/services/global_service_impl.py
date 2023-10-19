from src.application.services.global_service import GlobalService
from src.domain.services.global_data_aggregation_service import GlobalDataAggregationService


class GlobalServiceImpl(GlobalService):  # landing page
    def __init__(self,
                 global_data_aggregation_service: GlobalDataAggregationService
                 ):
        self.global_data_aggregation_service = global_data_aggregation_service

    def get_global_data(self):
        geo_data = self.global_data_aggregation_service.get_global_data()
        return geo_data

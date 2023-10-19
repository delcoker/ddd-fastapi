from src.application.services.orchestrator_service import OrchestratorService
from src.domain.repositories.api.api_repository import ApiRepository
from src.domain.repositories.db.user_repository import UserRepository
import functional as pyfunctional


class OrchestratorServiceImpl(OrchestratorService):
    def __init__(self, api_repository: ApiRepository, user_repository: UserRepository):
        self.api_repository = api_repository
        self.user_repository = user_repository

    def get_functional_data(self) -> [float]:
        numbers_less_10_plus_1 = pyfunctional.seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).map(
            lambda number: number * 2).filter(
            lambda number: number < 10).map(
            lambda number: self.multipy_by_2(number)).map(
            self.divide_by_2).list()

        return numbers_less_10_plus_1

    def get_api_data(self):
        api_data = self.api_repository.fetch_data()
        api_json = [todo.json() for todo in api_data]
        return api_json

    def get_db_data(self):
        db_data = self.user_repository.get_users()
        db_json = [{'id': u.id, 'username': u.username, 'email': u.email} for u in db_data]
        return db_json

    @staticmethod
    def add_1(number):
        return number + 1

    @staticmethod
    def divide_by_2(number):
        return number / 2.0

    @staticmethod
    def multipy_by_2(number):
        return number * 2.0

from src.infrastructure.models.db.user_dao import UserDao
from src.infrastructure.services.db_service import DatabaseService
from src.domain.repositories.db.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):

    def __init__(self, db_service: DatabaseService):
        self.db_service = db_service

    # def get_users(self, db: Session, skip: int = 0, limit: int = 100):
    def get_users(self):
        return (next(self.db_service.get_orm())
                .query(UserDao)
                # .offset(skip)
                # .limit(limit)
                .all())

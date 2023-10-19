# from typing import List, Any
# from fastapi import FastAPI
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from databases import Database
#
# from src.infrastructure.services.db_service import DatabaseService
#
# Base = declarative_base()
# metadata = MetaData()
#
# colours = {
#     'red': '\033[31m',
#     'green': '\033[32m',
#     'yellow': '\033[33m',
#     'blue': '\033[34m',
#     'magenta': '\033[35m',
#     'cyan': '\033[36m',
#     'white': '\033[37m',
#     'reset': '\033[0m'
# }
#
#
# class DatabaseServiceImpl(DatabaseService):
#     def __init__(self, app: FastAPI, db_uri: str):
#         self.db_uri = db_uri
#         self.engine = create_engine(db_uri)
#         self.database = Database(db_uri)
#         self.metadata = metadata
#
#         # Register the event handlers
#         # app.add_event_handler("startup", self.connect)
#         # app.add_event_handler("shutdown", self.disconnect)
#
#     def connect(self):
#         """Connect to the database."""
#         self.database.connect()
#
#     def disconnect(self):
#         """Disconnect from the database."""
#         self.database.disconnect()
#
#     def get_db(self):
#         """Retrieve the initialized databases instance.
#         :return: databases instance if initialized, else None.
#         """
#         return self.database
#
#     @classmethod
#     def from_uri(cls, app: FastAPI, db_uri: str):
#         return cls(app, db_uri)
#
#     async def fetch_all_users(self) -> Any:
#         query = "SELECT id, username, email FROM user"
#         results = await self.database.fetch_all(query)
#         users = [{"id": result[0], "username": result[1], "email": result[2]} for result in results]
#         return users

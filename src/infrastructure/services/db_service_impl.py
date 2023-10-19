import os
from typing import Optional, Dict

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from src.infrastructure.services.db_service import DatabaseService


class DatabaseServiceImpl(DatabaseService):

    def __init__(self, host: str, instance: str, username: str, password: str, database: str, port: int, driver: str,
                 tls: bool = False):
        inst = "\\" + instance if instance else ''
        db_uri = URL("mssql+pyodbc",
                     host=f'{host}{inst}',
                     username=username,
                     password=password,
                     database=database,
                     port=port,
                     query={
                         "driver": driver,
                         'TrustServerCertificate': tls
                     })
        self.engine = create_engine(db_uri)
        self.OrmSession = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @classmethod
    def from_uri(cls, db_uri: str):
        instance = cls.__new__(cls)
        instance.engine = create_engine(db_uri)
        instance.OrmSession = sessionmaker(autocommit=False, autoflush=False, bind=instance.engine)
        return instance

    def get_orm(self):
        orm = self.OrmSession()
        try:
            yield orm
        finally:
            orm.close()

    def execute_raw_query(self, query: str) -> bool:
        try:
            with self.engine.connect() as connection:
                connection.execute(text(query))
            print(f"Successfully executed query: {query[:100]}...")
            return True
        except Exception as e:
            print(f"Error executing query. Error: {e}")
            return False

    def execute_sql_script(self, script_path: str, replacements: Optional[Dict[str, str]] = None) -> Optional[
        Exception]:
        with open(script_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()

            # Perform text replacements if provided
            if replacements:
                for old_text, new_text in replacements.items():
                    sql_script = sql_script.replace(old_text, new_text)

            try:
                # with self.engine.connect() as connection:
                #     connection.execute(text(f"SET IDENTITY_INSERT RBP_trigger_result ON")) # if you must allow identity insert

                with self.engine.connect() as connection:
                    connection.execute(text(sql_script))
                print(f"Executed script: {script_path}")
                return None
            except Exception as e:
                print(f"Error executing script: {script_path}. Error: {e}")
                return e

    def execute_sql_scripts_from_directory(self, directory_path: str,
                                           replacements: Optional[Dict[str, str]] = None) -> None:
        for script_name in sorted(os.listdir(directory_path)):
            if script_name.endswith('.sql'):
                self.execute_sql_script(os.path.join(directory_path, script_name), replacements)

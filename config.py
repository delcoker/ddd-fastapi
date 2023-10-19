import os

from dotenv import load_dotenv

ENVIRONMENT = os.getenv("ENVIRONMENT", default="dev")
if ENVIRONMENT == "prod":
    load_dotenv(".env")
else:
    load_dotenv(".env.dev")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'your_secret_key'
DEBUG = False

# delete this section after you start the project
DB_USER_EXAMPLE = 'db_name_db_user'
DB_PASSWORD_EXAMPLE = 'db_name_db_pass'
DB_HOST_EXAMPLE = 'db4free.net'
DB_PORT_EXAMPLE = 3306
DB_NAME_EXAMPLE = 'db_name_db'
# end section

SQLALCHEMY_MYSQL_DATABASE_URI = (f"mysql+pymysql"
                                 f"://{DB_USER_EXAMPLE}"
                                 f":{DB_PASSWORD_EXAMPLE}"
                                 f"@{DB_HOST_EXAMPLE}"
                                 f"/{DB_NAME_EXAMPLE}")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv('DB_DRIVER')
DB_INSTANCE = "\\" + os.getenv('DB_INSTANCE') if os.getenv('DB_INSTANCE') else ''
DB_TLS = os.getenv("DB_TLS")

try:
    if None in [DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT, DB_DRIVER, DB_INSTANCE]:
        raise ValueError("One or more environment variables are missing.")

except ValueError as e:
    print("Please create a .env file")

BIRD_ISLAND_ID = 32
GAZA_ID = 1010
WEST_BANK_ID = 1011

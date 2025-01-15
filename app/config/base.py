import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# .env File Load
load_dotenv()

class BaseConfig(BaseSettings):
    DB_TYPE: str = os.getenv("DB_TYPE", "sqlite")  # Base Value : SQLite

# SQLite Settings
class SQLiteConfig(BaseConfig):
    DATABASE_URL: str = os.getenv("DATABASE_URL_SQLITE", "")

# MySQL Settings
class MySQLConfig(BaseConfig):
    DATABASE_URL: str = os.getenv("DATABASE_URL_MYSQL", "")

# PostgreSQL Settings
class PostgreSQLConfig(BaseConfig):
    DATABASE_URL: str = os.getenv("DATABASE_URL_POSTGRESQL", "")

# Load settings according to DB_TYPE
def get_settings():
    db_type = os.getenv("DB_TYPE", "sqlite")
    if db_type == "mysql":
        return MySQLConfig()
    elif db_type == "postgresql":
        return PostgreSQLConfig()
    else:  # Base Value: SQLite
        return SQLiteConfig()

# Creating a settings Object
settings = get_settings()
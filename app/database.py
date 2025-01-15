from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.base import settings

# Creating a Database Engine
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False} if settings.DB_TYPE == "sqlite" else {})

# Creating a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

from user_image_api.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_SCHEMA, DB_USER


DB_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DB_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database Table and schema.
def config_database_schema():
    try:
        if not engine.dialect.has_schema(engine, DB_SCHEMA):  # Verify Schema
            engine.execute(CreateSchema(DB_SCHEMA))
        Base.metadata.create_all(bind=engine, checkfirst=True)
    except SQLAlchemyError as err:
        logger.error(f"[-] SQLALCHEMY: ERROR DETECTED IN THE ORM OR DATABASE. {err}")


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

from fastapi import FastAPI
from loguru import logger

from user_image_api.config import DESCRIPTION, TITLE, VERSION
from user_image_api.config.database import config_database_schema
from user_image_api.exception import config_exception
from user_image_api.router import image, user, welcome

__version__ = VERSION


def run_api():
    api = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION
    )

    config_database_schema()
    api = config_exception(api)

    api.include_router(welcome.router, tags=['Welcome to api user image'])
    api.include_router(user.router, tags=['User'])
    api.include_router(image.router, tags=['Image'])

    logger.info("API is Works!")
    return api

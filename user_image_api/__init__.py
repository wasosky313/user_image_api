from fastapi import FastAPI
from loguru import logger

from user_image_api.config.database import config_database_schema
from user_image_api.exception import config_exception
from user_image_api.router import welcome, user, image

from user_image_api.config import VERSION, DESCRIPTION, TITLE

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
    api.include_router(user.router, tags=['Add and Update user'])
    api.include_router(image.router, tags=['Add user image'])

    logger.info("API is Works!")
    return api

from fastapi import FastAPI
from loguru import logger

from user_image_api.router import welcome, user

from user_image_api.config import VERSION, DESCRIPTION, TITLE

__version__ = VERSION


def run_api():
    api = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION
    )

    api.include_router(welcome.router, tags=['Welcome to api user image'])
    api.include_router(user.router, tags=['Add and Update user'])

    logger.info("API is Works!")
    return api

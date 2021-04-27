
from loguru import logger


class ApiException(Exception):
    def __init__(self, code: int = 404, message: str = "OPERATION ERROR"):
        self.code = code
        self.message = message
        try:
            logger.level("EXCEPTION", no=25, color="<red><bold>")
        except TypeError:
            pass
        logger.log("EXCEPTION", f'{message}, STATUS: {code}')


class UniqueException(ApiException):
    def __init__(self):
        message = 'UNIQUE CONSTRAINT: THE VALUE ALREADY EXISTS IN THE DATABASE'
        super().__init__(409, message)

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


class SQLAlchemyException(ApiException):
    def __init__(self):
        message = "SQLAlchemy ERROR: COULD NOT CONNECT TO SERVER"
        super().__init__(409, message)


class NoExistException(ApiException):
    def __init__(self):
        message = 'NOT FOUND: THE VALUE NO EXIST IN THE DATABASE'
        super().__init__(409, message)


class Base64Exception(ApiException):
    def __init__(self):
        message = 'WRONG BASE64 FORMAT'
        super().__init__(401, message)


class TypeException(ApiException):
    def __init__(self):
        message = "ERROR: THE VALUE ISN'T int"
        super().__init__(401, message)

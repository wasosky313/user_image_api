from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .base import ApiException


def config_exception(api):
    @api.exception_handler(ApiException)
    def api_exception(request: Request, exception: ApiException):
        return JSONResponse(status_code=exception.code,
                            content={"message": exception.message})

    @api.exception_handler(HTTPException)
    def http_exception(request: Request, exception: HTTPException):
        message = {404: "Address not found", 405: "Method not allowed"}
        return JSONResponse(
            status_code=exception.status_code,
            content={"message": message[exception.status_code]}
        )

    @api.exception_handler(RequestValidationError)
    def validation_exception(request, exception):
        return JSONResponse(status_code=422,
                            content={"message": "Error mapping"
                                                "response object"})

    return api

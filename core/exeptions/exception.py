import fastapi as fa
import abc
import typing


class BaseError(abc.ABC, Exception):
    status_code: typing.Optional[int] = None
    message: typing.Optional[str] = None

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class NotFound(BaseError):
    status_code = 404
    message = "Not found"


async def api_exception_handler(_, exc: BaseError) -> fa.responses.JSONResponse:
    return fa.responses.JSONResponse(
        status_code=exc.status_code, content={"message": exc.message}
    )


exeption_handlers: dict[typing.Type[Exception], typing.Callable] = {
    BaseError: api_exception_handler
}

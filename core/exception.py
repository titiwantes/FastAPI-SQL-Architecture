import fastapi as fa


async def http_exception_handler(request: fa.Request, exc: fa.HTTPException):
    return fa.responses.JSONResponse(
        status_code=exc.status_code, content={"message": exc.detail}
    )


async def validation_exception_handler(request: fa.Request, exc: fa.HTTPException):
    return fa.responses.JSONResponse(
        status_code=400, content={"message": "Validation error", "details": exc.detail}
    )

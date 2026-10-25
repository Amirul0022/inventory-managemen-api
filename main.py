from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from routers import items, transactions

app = FastAPI(title="Sistem Inventori & Gudang API", version="1.0.0")

app.include_router(items.router)
app.include_router(transactions.router)

@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    formatted = [
        {"field": " -> ".join(str(l) for l in e["loc"]),
         "msg": e["msg"]}
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "code": "VALIDATION_ERROR",
            "path": request.url.path,
            "details": formatted
        }
    )

@app.get("/", tags=["Root"])
async def root():
    return {"service": "Gudang API", "status": "running"}

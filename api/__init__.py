from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from api.common.logger_config import logger
from api.features.customers.routes import customer_router
from api.features.countries.routes import country_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Custom handler to log all HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException: {exc.detail} (status_code={exc.status_code}) on path {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

logger.info("Starting API")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer_router, prefix="/customers")
app.include_router(country_router, prefix="/countries")
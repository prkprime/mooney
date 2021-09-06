import logging
import sys

from fastapi import FastAPI
from decouple import config, UndefinedValueError
from starlette.middleware.cors import CORSMiddleware

from .models import Income
from .database import create_db_and_tables


def check_env_vars():
    try:
        config("database_url")
    except UndefinedValueError as e:
        sys.exit(e)
    except Exception as e:
        sys.exit(e)


check_env_vars()

from app.api.v1.api import api_router

logging.basicConfig(
    format="[%(levelname)s] (%(asctime)s) %(module)s:%(pathname)s:%(funcName)s:%(lineno)s:: %(message)s",
    level=logging.INFO,
    datefmt="%d-%m-%y %H:%M:%S",
    stream=sys.stdout,
)

app = FastAPI(title="Mooney", openapi_url="/api/v1/openapi.json")

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(api_router, prefix="/api/v1")

logging.info("Starting application")

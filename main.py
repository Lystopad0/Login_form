from fastapi import FastAPI
from auth import auth
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import inspect
import re
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi

app = FastAPI()




@AuthJWT.load_config
def get_config():
    return Settings()


app.include_router(auth)

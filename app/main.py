from fastapi import FastAPI
from app.routers import test

fastAPI = FastAPI()
fastAPI.include_router(test.router)
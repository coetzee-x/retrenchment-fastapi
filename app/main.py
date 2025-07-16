from fastapi import FastAPI
from app.routers import auth_router, test, user_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(test.router)
app.include_router(auth_router.router)
app.include_router(user_router.router)
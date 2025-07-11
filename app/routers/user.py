from fastapi import APIRouter, Depends
from app.dependencies.database import get_db
from app.models.user import User
from app.services.user_service import get_current_user

router = APIRouter(prefix="/users")

@router.get("/")
def get_users(user: User = Depends(get_current_user)):
    return user
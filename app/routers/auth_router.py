from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.login_schema import LoginSchema
from app.services import user_service
from app.services.user_service import *

router = APIRouter(prefix="/auth")

@router.post("/login")
def login(
    login_schema: LoginSchema, 
    db: Session = Depends(get_db)):
    try:
        print("")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.post("/register")
def register(
    register_schema: RegisterSchema, 
    db: Session = Depends(get_db)):
    try:
        return user_service.register_user(register_schema=register_schema, db=db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")





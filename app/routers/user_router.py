from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.create_registration_link_schema import CreateRegistrationLinkSchema
from app.services import user_service

router = APIRouter(prefix="/users")

@router.post("/create-registration-link")
def send_registration_email(
    schema: CreateRegistrationLinkSchema,
    db: Session = Depends(get_db)):
    try:
        return user_service.create_registration_link(schema, db)
    except Exception as ex:
        print(ex)
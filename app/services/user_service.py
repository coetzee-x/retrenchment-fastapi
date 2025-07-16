import smtplib
from fastapi import Depends
import jwt
import os
from jwt import ExpiredSignatureError, InvalidTokenError
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from app.dependencies.database import get_db
from app.models.company import Company
from app.models.company_user import CompanyUser
from app.models.registration_link_model import RegistrationLinkModel
from app.models.user import User
from app.repositories import company_repository, role_repository, user_repository
from app.schemas.company_schema import CompanySchema
from app.schemas.create_registration_link_schema import CreateRegistrationLinkSchema
from app.schemas.http_exception_detail import HttpExceptionDetail
from app.schemas.login_schema import LoginSchema
from app.schemas.register_schema import RegisterSchema
from app.services import utility_service
from app.services.email_sender_service import EmailSenderService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")


# This function verifies the JWT token and retrieves the current user from the database.
def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)], 
        db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, str(os.getenv("JWT_DECODE_PUBLIC_KEY")), algorithms=[str(os.getenv("JWT_ALGORITHM"))])
        user_id = int(payload["sub"])
        if not user_id:
            HttpExceptionDetail(status_code=status.HTTP_401_UNAUTHORIZED, error_code="invalid_token", message="Invalid token").raise_exception()
        user = db.execute(select(User).where(User.id == user_id)).scalars().first()
        if not user:
            HttpExceptionDetail(status_code=status.HTTP_404_NOT_FOUND, error_code="not_found", message="User not found").raise_exception()
        return user
    except ExpiredSignatureError:
        HttpExceptionDetail(status_code=status.HTTP_401_UNAUTHORIZED, error_code="token_expired", message="Token expired").raise_exception()
    except InvalidTokenError:
         HttpExceptionDetail(status_code=status.HTTP_401_UNAUTHORIZED, error_code="invalid_token", message="Invalid token").raise_exception()
    except Exception:
        HttpExceptionDetail(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, error_code="internal_error", message="Internal error").raise_exception()

# This function creates a JWT token for the user.
def create_user_token(user: User) -> dict:
    private_key = str(os.getenv("JWT_ENCODE_PRIVATE_KEY"))
    token = jwt.encode({"sub": str(user.id), "email": user.email}, private_key, algorithm=str(os.getenv("JWT_ALGORITHM")))
    return {
        "access-token": token,
        "token-type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email
        }
    }

# This function registers a new user in the system. 
def register_user(
        register_schema: RegisterSchema, 
        db: Session) -> dict: 
    company = company_repository.get_company_by_guid(guid=register_schema.company_guid, db=db)
    if not company: 
        raise LookupError("The company does not exist")
    user = user_repository.get_user_by_email(email = register_schema.email, db=db)
    if not user:
        user = user_repository.register_new_user(email=register_schema.email, password=utility_service.hash_password(register_schema.password), company=company, db=db)
    else:
        companies = user_repository.get_user_companies(email=register_schema.email, db=db)
        if not utility_service.compare_passwords(register_schema.password, str(user.password)):
            raise ValueError("Incorrect email or password")
        if companies and not any(comp.guid == register_schema.company_guid for comp in companies):
            user = user_repository.register_existing_user(user_id=int(str(user.id)), company_id=int(str(company.id)), db=db)
    return create_user_token(user)

def login_user(
        login_schema: LoginSchema, 
        db:Session) -> dict:
    user = user_repository.get_user_by_email_and_password(email=login_schema.email, password="", db=db)
    if not user:
        raise LookupError("Incorrect email or password")
    return create_user_token(user)




def create_registration_link(
    schema: CreateRegistrationLinkSchema,
    db: Session) -> int:
    company = company_repository.get_company_by_id(schema.company_id, db)
    if not company: raise LookupError("Company not found")
    role = role_repository.get_role_by_id(schema.role_id, db)
    if not role: raise LookupError("Role not found")
    registration_link = user_repository.create_registration_link(
        firstname=schema.firstname, 
        lastname=schema.lastname, 
        email=schema.email, 
        company_id=company.id, 
        role_id=role.id,
        db=db)
    EmailSenderService.send_email("xander.coetzee@smollan.com","test subject", "test body")
    
        
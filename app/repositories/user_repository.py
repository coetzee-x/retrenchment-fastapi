from sqlalchemy.orm import Session
from app.models.company import Company
from app.models.company_user import CompanyUser
from app.models.user import User

def get_user_companies(
        email: str, 
        db: Session) -> list[Company] | None:
    return (
        db.query(Company)
        .join(CompanyUser)
        .join(User)
        .filter(User.email == email).all())

def register_new_user(
        email: str,
        password: str, 
        company: Company,
        db: Session) -> User | None:
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    user.companies.append(company)
    db.commit()
    return user

def register_existing_user(
        user_id: int,
        company_id: int,
        db: Session) -> User | None:
    user_company = CompanyUser(user_id=user_id,company_id=company_id)
    db.add(user_company)
    db.commit()
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first())

def get_user_by_email_and_password(
        email: str, 
        password: str,
        db: Session) -> User | None:
    return (
        db.query(User)
        .filter(User.email == email)
        .filter(User.password == password)
        .first())

def get_user_by_email(
        email: str, 
        db: Session) -> User | None:
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


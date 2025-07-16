from sqlalchemy.orm import Session
from app.models.company import Company

def get_company_by_guid(
        guid: str, 
        db: Session) -> Company | None:
        return db.query(Company).filter(Company.guid == guid.strip()).first()

def get_company_by_id(
        id: int, 
        db: Session) -> Company | None:
        return db.query(Company).filter(Company.id == id).first()
    
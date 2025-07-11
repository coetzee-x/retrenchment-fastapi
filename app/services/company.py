from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.models.company import Company
from app.repositories import company_repository
from app.schemas.company_schema import CompanySchema

def get_company_by_guid(
        guid: str, 
        db: Session = Depends(get_db)) -> str | None:
    
    company = company_repository.get_company_by_guid(guid=guid, db=db)

    if not company:
        return None
    
    return ""

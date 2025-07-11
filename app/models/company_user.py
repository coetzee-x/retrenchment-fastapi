from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class CompanyUser(Base):
    __tablename__ = "company_user"
    user_id = Column(ForeignKey("users.id"), primary_key=True, nullable=False)
    company_id = Column(ForeignKey("companies.id"), primary_key=True, nullable=False)

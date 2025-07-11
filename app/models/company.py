from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.company_user import CompanyUser

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(55), nullable=False)
    short = Column(String(10), nullable=False)
    guid = Column(String(36), nullable=False)
    users = relationship("User", secondary="company_user", back_populates="companies")

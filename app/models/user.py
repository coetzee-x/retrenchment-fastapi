from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.company_user import CompanyUser

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(55), nullable=False)
    password = Column( String(255), nullable=False)
    companies = relationship("Company", secondary="company_user", back_populates="users")

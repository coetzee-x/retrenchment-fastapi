from sqlalchemy import Column, Integer, String
from app.models.base import Base

class RoleModel(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(15), nullable=False)
    description = Column(String(255), nullable=True)
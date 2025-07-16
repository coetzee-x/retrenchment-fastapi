from datetime import datetime
import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, Integer, String
from app.models.base import Base

class RegistrationLinkModel(Base):
    __tablename__ = "registration_links"
    id = Column(Integer, primary_key=True, nullable=False)
    created_on = Column(DateTime, default=datetime.now(), nullable=False)
    registered_on = Column(DateTime, default=datetime.now(), nullable=True)
    firstname = Column(String(55), nullable=False)
    lastname = Column(String(55), nullable=False)
    email = Column(String(55), nullable=False)
    company_id = Column(ForeignKey("companies.id"), nullable=False)
    role_id = Column(ForeignKey("roles.id"), nullable=False)
    guid = Column(UUID(), default=uuid.uuid4, nullable=False)
    used = Column(Boolean, default=False, nullable=False)
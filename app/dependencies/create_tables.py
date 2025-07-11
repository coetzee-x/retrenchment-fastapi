from app.dependencies.database import engine
from app.models.base import Base
from app.models.company_user import CompanyUser
from app.models.company import Company
from app.models.user import User
from app.models.role_model import RoleModel

Base.metadata.create_all(bind=engine)
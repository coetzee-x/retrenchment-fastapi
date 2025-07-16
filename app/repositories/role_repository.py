from sqlalchemy.orm import Session

from app.models.role_model import RoleModel

def get_roles(db: Session):
    return (db.query(RoleModel).all())

def get_role_by_id(id: int, db:Session) -> RoleModel | None:
    return (db.query(RoleModel)
            .filter(RoleModel.id == id)
            .first())
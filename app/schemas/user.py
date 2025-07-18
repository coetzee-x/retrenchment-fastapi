from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    password: str
    company_id: int
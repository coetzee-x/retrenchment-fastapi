from pydantic import BaseModel

class RegisterSchema(BaseModel):
    email: str
    password: str
    company_guid: str
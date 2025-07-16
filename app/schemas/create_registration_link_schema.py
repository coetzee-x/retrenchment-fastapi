from pydantic import BaseModel

class CreateRegistrationLinkSchema(BaseModel):
    firstname: str
    lastname: str
    email: str
    company_id: int
    role_id: int
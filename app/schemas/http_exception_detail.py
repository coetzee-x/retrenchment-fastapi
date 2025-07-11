from fastapi import HTTPException
from pydantic import BaseModel

class HttpExceptionDetail(BaseModel):
    status_code: int
    error_code: str
    message: str

    def raise_exception(self):
        raise HTTPException(
            status_code=self.status_code,
            detail={
                "error_code": self.error_code,
                "message": self.message
            }
        )
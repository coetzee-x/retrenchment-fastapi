from fastapi import APIRouter

router = APIRouter(prefix="/text")

@router.get("/")
def get_test()->str:
    return "Hello World!"

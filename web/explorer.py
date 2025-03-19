from fastapi import APIRouter

router = APIRouter(prefix="/explorer")


@router.get("")
@router.get("/")
def get_all():
    return "All explorers"

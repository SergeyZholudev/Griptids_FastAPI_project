from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

router = APIRouter(prefix="/explorer")


@router.get("")
@router.get("/")
def top():
    return service.get_all()


@router.get("/{name}")
def get_one(name):
    return service.get_one(name)

from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/explorer")
templates = Jinja2Templates(directory="templates")


@router.get("")
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "listOfExplorers": service.get_all()}
    )


@router.get("/{name}")
def get_one(request: Request, name: str):
    return templates.TemplateResponse(
        "one_name.html", {"request": request, "explorer": service.get_one(name)}
    )

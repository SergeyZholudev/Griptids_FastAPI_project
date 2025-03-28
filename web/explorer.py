from fastapi import APIRouter, Body, status
from model.explorer import Explorer
import data.explorer as expl

from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/explorer")
templates = Jinja2Templates(directory="templates")


@router.get("")
@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "listOfExplorers": expl.get_all()}
    )


@router.get("/{name}")
def get_one(request: Request, name: str):
    return templates.TemplateResponse(
        "one_name.html", {"request": request, "explorer": expl.get_one(name)}
    )


@router.post("/create")
def create(explorer: Explorer):
    expl.create(explorer)
    return {"input_data": explorer, "statusCode": status.HTTP_201_CREATED}

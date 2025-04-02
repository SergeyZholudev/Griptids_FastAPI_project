from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
import data.explorer as expl
from error import Missing, Duplicate

from starlette.requests import Request
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
    try:
        return templates.TemplateResponse(
            "one_name.html", {"request": request, "explorer": expl.get_one(name)}
        )
    except Missing as exc:
        return templates.TemplateResponse(
            "warning.html", {"request": request, "warning": exc.msg}
        )


@router.post("/create", status_code=201)
def create(explorer: Explorer):
    try:
        return expl.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

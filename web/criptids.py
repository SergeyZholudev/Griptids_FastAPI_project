from fastapi import APIRouter
from starlette.templating import Jinja2Templates
from service.criptids import Criptid as crip
from model.criptid import Criptid

from starlette.requests import Request


router = APIRouter(prefix="/criptids")
template = Jinja2Templates(directory="templates")


@router.get("")
@router.get("/")
def get_all(request: Request):
    return template.TemplateResponse(
        "criptids.html", {"request": request, "listOfCriptids": crip.get_all()}
    )


@router.get("/{name}")
def get_one(request: Request, name):
    return template.TemplateResponse(
        "criptids_one.html", {"request": request, "criptid": crip.get_one(name)}
    )


@router.post("/create", status_code=201)
def create(criptid: Criptid):
    return crip.create(criptid)

from fastapi import FastAPI
from web import explorer
import uvicorn

from starlette import middleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)
templates = Jinja2Templates(directory="templates")


_explorers = [
    ("Claude Hande", "GE", 45),
    ("Fritz HourherHoff", "GE", 42),
    ("Mike Clarke", "GB", 67),
]


@app.get("")
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "listOfExplorers": _explorers}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

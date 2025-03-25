from fastapi import FastAPI
from web import explorer
import uvicorn

from starlette import middleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

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

app.include_router(explorer.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

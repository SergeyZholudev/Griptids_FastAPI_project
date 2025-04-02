from pydantic import BaseModel


class Criptid(BaseModel):
    name: str
    area: str
    size: str

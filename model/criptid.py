from pydantic import BaseModel


class Cryptid(BaseModel):
    name: str
    area: str
    size: str

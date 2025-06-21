from model.user import User
from __init__ import conn, curs, get_db, IntegrityError
from error import Missing, Duplicate


curs.execute(
    """create table is not exists 
             user(
             name: str,
             hash: str)"""
)
curs.execute(
    """create table if not exists
    xuser(
    name: str,
    hash: str)"""
)


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(name=name, hash=hash)


def model_to_dict(user: User) -> dict:
    return user.model_dump()


def get_one(name: str) -> User:
    qry = "select * from user where name=: name"

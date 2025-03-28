# from .__init__ import conn, curs
from model.explorer import Explorer
import sqlite3

DB_NAME = "cryptid.db"
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
curs = conn.cursor()


def init():
    curs.execute("create table if not exist explorer(name, country)")


def row_to_obj(row: tuple) -> Explorer:
    """deserializtion"""
    name, country = row
    return Explorer(name, country)


def obj_to_dict(explorer: Explorer) -> dict:
    """serialization"""
    expl = explorer.model_dump()
    return expl


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    res = curs.execute(qry)
    return res


def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row


def create(explorer: Explorer):
    qry = "insert into explorer(name, country) values(:name, :country)"
    params = obj_to_dict(explorer)
    curs.execute(qry, params)

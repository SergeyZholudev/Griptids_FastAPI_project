from .__init__ import conn, curs, IntegrityError
from model.explorer import Explorer
from error import Missing, Duplicate

curs.execute(
    """create table if not exists explorer(
             name text primary key,
             country text)"""
)


def row_to_obj(row: tuple) -> Explorer:
    """deserializtion"""
    name, country = row
    return Explorer(name=name, country=country)


def obj_to_dict(explorer: Explorer) -> dict:
    """serialization"""
    expl = explorer.model_dump()
    return expl


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_obj(row) for row in curs.fetchall()]


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

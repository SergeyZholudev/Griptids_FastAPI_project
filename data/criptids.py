from .__init__ import curs, conn
from model.criptid import Criptid

curs.execute(
    """create table if not exists criptids(
             name text primary key,
             area text,
             size text)"""
)


def row_to_obj(row: tuple) -> Criptid:
    name, area, size = row
    return Criptid(name=name, area=area, size=size)


def obj_to_row(criptid: Criptid):
    return criptid.model_dump()


def get_all() -> list[Criptid]:
    qry = "select * from criptids"
    curs.execute(qry)
    return [row_to_obj(row) for row in curs.fetchall()]


def get_one(name):
    qry = "select * from criptids where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_obj(row)


def create(criptid: Criptid) -> Criptid:
    qry = "insert into criptids(name, area, size) values(:name, :area, :size)"
    params = obj_to_row(criptid)
    curs.execute(qry, params)
    return get_one(criptid.name)

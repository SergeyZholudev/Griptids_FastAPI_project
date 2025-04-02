import data.criptids as crip
from model.criptid import Criptid


def get_all():
    return crip.get_all()


def get_one(name):
    return crip.get_one(name)


def create(criptid: Criptid):
    return crip.create(criptid)

import os
import pytest

from model.explorer import Explorer
from error import Missing, Duplicate

# set this vefore data imports below for data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory"
from data import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Sergey", country="RU")


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)


def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("boxturtle")

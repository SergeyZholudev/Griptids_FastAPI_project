from model.explorer import Explorer

_explorers = [
    Explorer(name="Claude Hande", country="GE", age=45),
    Explorer(name="Fritz HourherHoff", country="GE", age=42),
    Explorer(name="Mike Clarke", country="GB", age=67),
    Explorer(name="Michael Shumaher", country="GE", age=56),
]


def get_all() -> list[Explorer]:
    """Return of all explorers"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer

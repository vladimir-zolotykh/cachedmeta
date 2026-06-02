#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class NullMeta(type):
    def __repr__(cls):
        repr = getattr(cls, "repr", "Null")
        # return "Null"
        return repr


class Null(metaclass=NullMeta):
    def __new__(cls, *args, **kwds):
        raise RuntimeError(f"{cls} cannot be instantiated")


class Missing(Null):
    repr = "Missing"


if __name__ == "__main__":
    assert Null is Null
    print(Null)
    print(Missing)
    try:
        null = Null()
    except RuntimeError as exc:
        print(exc)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Any
from operator import itemgetter


class TupleMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        fields = clsdict.get("_fields", [])
        for i, name in enumerate(fields):
            setattr(cls, name, property(itemgetter(i)))


class MyTuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args):
        if (n := len(cls._fields)) != len(args):
            raise TypeError(f"{cls.__name__} expects {n} arguments")
        return super().__new__(cls, args)


class Exercise(MyTuple):
    _fields = ["name", "weight", "reps"]


def as_csv(t: MyTuple) -> tuple[Any, ...]:
    return ", ".join((f"{f}={getattr(t, f)!r}" for f in t._fields))


if __name__ == "__main__":
    exer = Exercise("bench press", 50.0, 4)
    print(as_csv(exer))

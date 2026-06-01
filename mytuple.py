#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from operator import itemgetter


class TupleMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        print(f"__init__ {cls}")
        super().__init__(cls, clsname, bases, clsdict)
        for i, name in enumerate(clsdict.get("_fields", [])):
            setattr(cls, name, property(itemgetter(i)))


class MyTuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args):
        print(f"__new__ {cls}")
        if (n := len(cls._fields)) != len(args):
            raise TypeError(f"{cls.__name__} expects {n} arguments")
        return super().__new__(*args)


class Exercise(MyTuple):
    _fields = ["name", "weight", "reps"]


if __name__ == "__main__":
    exer = Exercise("bench press", 50.0, 4)
    print(exer)

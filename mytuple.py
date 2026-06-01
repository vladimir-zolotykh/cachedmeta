#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from operator import itemgetter


class TupleMeta(type):
    def __init__(cls, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        fields = clsdict.get("_fields", [])
        if fields:
            print(f"TupleMeta.__init__ {cls}")
        for i, name in enumerate(fields):
            setattr(cls, name, property(itemgetter(i)))


class MyTuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args):
        print(f"MyTuple.__new__ {cls}")
        if (n := len(cls._fields)) != len(args):
            raise TypeError(f"{cls.__name__} expects {n} arguments")
        return super().__new__(cls, args)


class Exercise(MyTuple):
    _fields = ["name", "weight", "reps"]


if __name__ == "__main__":
    exer = Exercise("bench press", 50.0, 4)
    print(exer)

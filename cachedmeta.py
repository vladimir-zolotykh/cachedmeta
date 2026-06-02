#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import defaultdict


class CachedMeta(type):
    _instances = defaultdict(defaultdict)

    def __call__(cls, *args, **kwds):
        tup = tuple(args)
        if cls in type(cls)._instances and tup in type(cls)._instances[cls]:
            return type(cls)._instances[cls][tup]
        else:
            obj = super().__call__(*args, **kwds)
            type(cls)._instances[cls][tup] = obj
            return obj


class CachedData(metaclass=CachedMeta):
    pass


class Person(CachedData):
    def __init__(self, name, age, salary):
        print(f"Initializing {name!r}")
        self.name = name
        self.age = age
        self.salary = salary


if __name__ == "__main__":
    jim = Person("James Patterson", 42, 78000)
    dan = Person("Daniel Okonkwo", 29, 112000)
    ed1 = Person("Eduardo Flores", 61, 54000)

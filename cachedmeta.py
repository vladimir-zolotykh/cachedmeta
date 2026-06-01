#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class CachedMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls in type(cls)._instances:
            objects = type(cls)._instances[cls]
            tup = tuple(args)
            if tup in objects:
                return objects[tup]
            else:
                obj = super().__call__(*args, **kwds)
                objects[tup] = obj
                return obj
        else:
            tup = tuple(args)
            obj = super().__call__(*args, **kwds)
            type(cls)._instances = dict(key=tup, value=obj)
            return obj


class CachedData(metaclass=CachedMeta):
    pass


class Person(CachedData):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


if __name__ == "__main__":
    # jim = Person("James Patterson", 42, 78000)
    # dan = Person("Daniel Okonkwo", 29, 112000)
    ed = Person("Eduardo Flores", 61, 54000)
    print(ed.__dict__)

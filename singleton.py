#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> g1 = Logger()
Initializing Logger
>>> g2 = Logger()
>>> assert g1 is g2
>>> m1 = Module()
Initializing Module
>>> m2 = Module()
>>> assert m1 is m2
"""


class Singleton(type):
    _instances = {}

    def __call__(cls):
        if cls in type(cls)._instances:
            return type(cls)._instances[cls]
        else:
            obj = super().__call__()
            type(cls)._instances[cls] = obj
            return obj


class Logger(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")


class Module(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

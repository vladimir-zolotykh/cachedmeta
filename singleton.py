#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    _instances = {}

    def __call__(cls):
        if cls in Singleton._instances:
            return Singleton._instances[cls]
        else:
            obj = super().__call__()
            Singleton._instances[cls] = obj
            return obj


class Logger(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")


class Module(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")


if __name__ == "__main__":
    g1 = Logger()
    g2 = Logger()
    assert g1 is g2
    m1 = Module()
    m2 = Module()
    assert m1 is m2

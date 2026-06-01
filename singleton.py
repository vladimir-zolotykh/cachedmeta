#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    _instance = None

    def __call__(cls):
        if Singleton._instance:
            return Singleton._instance
        else:
            cls = super().__call__()
            Singleton._instance = cls
            return cls


class Logger(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing {self.__class__.__name__}")


if __name__ == "__main__":
    g1 = Logger()
    g2 = Logger()
    assert g1 is g2

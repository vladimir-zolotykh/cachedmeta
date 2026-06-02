#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Callable
import math


class LazyProperty:
    def __init__(self, func: Callable):
        self._func = func

    def __set_name__(self, owner, name):
        # setting _name <- area
        # setting _name <- circumference

        print(f"setting _name <- {name}")
        self._name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        saved_val = instance.__dict__.get(self._name, None)
        if not (saved_val is None):
            return instance.__dict__[self._name]
        val = self._func(instance)
        instance.__dict__[self._name] = val
        return val


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @LazyProperty
    def area(self):
        print("calculating area")
        return math.pi * self._radius**2

    @LazyProperty
    def circumference(self):
        print("calculating circumference")
        return 2 * math.pi * self._radius


if __name__ == "__main__":
    c = Circle(10.2)

    print(c.area)
    print(c.circumference)
    print(c.area)

import pytest

from cachedmeta import Person


def test_same_arguments_return_same_instance():
    p1 = Person("James Patterson", 42, 78000)
    p2 = Person("James Patterson", 42, 78000)

    assert p1 is p2


def test_different_arguments_return_different_instances():
    p1 = Person("James Patterson", 42, 78000)
    p2 = Person("Daniel Okonkwo", 29, 112000)

    assert p1 is not p2


def test_attributes_are_preserved():
    p = Person("James Patterson", 42, 78000)

    assert p.name == "James Patterson"
    assert p.age == 42
    assert p.salary == 78000


def test_init_called_only_once(capsys):
    Person("Eduardo Flores", 61, 54000)
    Person("Eduardo Flores", 61, 54000)

    captured = capsys.readouterr()

    assert captured.out.count("Initializing 'Eduardo Flores'") == 1

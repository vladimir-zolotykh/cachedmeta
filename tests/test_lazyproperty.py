import math

from lazyproperty import Circle


def test_lazy_properties(capsys):
    c = Circle(10.2)

    area1 = c.area
    circumference = c.circumference
    area2 = c.area

    assert area1 == math.pi * 10.2**2
    assert circumference == 2 * math.pi * 10.2
    assert area1 == area2

    captured = capsys.readouterr()

    assert captured.out.count("calculating area") == 1
    assert captured.out.count("calculating circumference") == 1

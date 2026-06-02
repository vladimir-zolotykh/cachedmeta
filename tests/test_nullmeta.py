import pytest

from nullmeta import Null, Missing


def test_nullmeta(capsys):
    assert Null is Null

    print(Null)
    print(Missing)

    with pytest.raises(RuntimeError) as exc_info:
        Null()

    print(exc_info.value)

    captured = capsys.readouterr()

    assert captured.out == ("Null\n" "Missing\n" "Null cannot be instantiated\n")

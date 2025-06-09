""" Tests for the number module.
This module contains unit tests for the `Number` class in the Sudoku game.
"""
from core.number import Number
import pytest

# ----------------------------------------------------------------------
# METHOD __init__
# ----------------------------------------------------------------------
def test_default_initialization():
    n = Number()
    assert n.get_value() == 0
    assert not n.is_fixed()
    assert str(n) == "."

def test_valid_initialization():
    for v in range(1, 10):  # 0 excluded because it is forbidden to be fixed
        n = Number(v, True)
        assert n.get_value() == v
        assert n.is_fixed() is True

def test_invalid_value_initialization():
    with pytest.raises(ValueError):
        Number(-1)
    with pytest.raises(ValueError):
        Number(10)
    with pytest.raises(TypeError):
        Number("a")  # type: ignore

def test_invalid_fixed_type():
    with pytest.raises(TypeError):
        Number(1, fixed="yes")  # type: ignore

def test_cannot_fix_zero_on_init():
    with pytest.raises(PermissionError):
        Number(0, fixed=True)

# ----------------------------------------------------------------------
# METHOD __str__
# ----------------------------------------------------------------------
def test_str_representation():
    assert str(Number(0)) == "."
    for v in range(1, 10):
        assert str(Number(v)) == str(v)

# ----------------------------------------------------------------------
# METHOD set_value
# ----------------------------------------------------------------------
def test_set_value_valid():
    n = Number()
    n.set_value(5)
    assert n.get_value() == 5
    n.set_value(0)
    assert n.get_value() == 0

def test_set_value_invalid():
    n = Number()
    with pytest.raises(ValueError):
        n.set_value(-1)
    with pytest.raises(ValueError):
        n.set_value(10)
    with pytest.raises(TypeError):
        n.set_value("b")

def test_set_value_fixed():
    n = Number(3, fixed=True)
    with pytest.raises(PermissionError):
        n.set_value(4)

# ----------------------------------------------------------------------
# METHOD clear_value
# ----------------------------------------------------------------------
def test_clear_value():
    n = Number(5)
    n.clear_value()
    assert n.get_value() == 0

def test_clear_value_fixed():
    n = Number(5, fixed=True)
    with pytest.raises(PermissionError):
        n.clear_value()

# ----------------------------------------------------------------------
# METHOD is_fixed, lock
# ----------------------------------------------------------------------
def test_is_fixed_and_lock():
    n = Number(2)
    assert not n.is_fixed()
    n.lock()
    assert n.is_fixed()
    with pytest.raises(PermissionError):
        n.lock()

def test_cannot_lock_zero():
    n = Number(0)
    with pytest.raises(PermissionError):
        n.lock()

# _is_valid (indirectly tested through init/set_value)
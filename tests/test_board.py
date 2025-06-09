""" Tests for the board module.
This module contains unit tests for the `Board` class in the Sudoku game.
"""
from core.board import Board
from core.number import Number
import pytest

# ----------------------------------------------------------------------
# METHOD __init__
# ----------------------------------------------------------------------
def test_board_default_init():
    b = Board()
    for i in range(9):
        for j in range(9):
            assert b.get_number(i, j) == 0

def test_board_init_with_valid_grid():
    grid = [[Number((i*9+j)%10) for j in range(9)] for i in range(9)]
    b = Board(grid)
    for i in range(9):
        for j in range(9):
            assert b.get_number(i, j) == (i*9+j)%10

def test_board_init_invalid_grid_shape():
    grid = [[Number(0) for _ in range(8)] for _ in range(9)]
    with pytest.raises(ValueError):
        Board(grid)
    grid = [[Number(0) for _ in range(9)] for _ in range(8)]
    with pytest.raises(ValueError):
        Board(grid)

def test_board_init_invalid_grid_type():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    with pytest.raises(TypeError):
        Board(grid)
    grid = [Number(0) for _ in range(9)]
    with pytest.raises(TypeError):
        Board(grid)

# ----------------------------------------------------------------------
# METHOD __str__
# ----------------------------------------------------------------------
def test_board_str_empty():
    b = Board()
    s = str(b)
    assert s.count(".") == 81
    assert s.count("\n") == 8

def test_board_str_partial():
    b = Board()
    b.set_number(0, 0, 5)
    b.set_number(1, 1, 3)
    s = str(b)
    assert "5" in s and "3" in s
    assert s.count(".") == 79

# ----------------------------------------------------------------------
# METHOD get_number, set_number, clear_number
# ----------------------------------------------------------------------
def test_get_set_clear_number():
    b = Board()
    b.set_number(0, 0, 7)
    assert b.get_number(0, 0) == 7
    b.clear_number(0, 0)
    assert b.get_number(0, 0) == 0

def test_set_number_invalid_index():
    b = Board()
    with pytest.raises(IndexError):
        b.set_number(9, 0, 1)
    with pytest.raises(IndexError):
        b.set_number(0, 9, 1)
    with pytest.raises(TypeError):
        b.set_number("a", 0, 1)
    with pytest.raises(TypeError):
        b.set_number(0, "b", 1)

def test_set_number_invalid_value():
    b = Board()
    with pytest.raises(ValueError):
        b.set_number(0, 0, 10)
    with pytest.raises(ValueError):
        b.set_number(0, 0, -1)
    with pytest.raises(TypeError):
        b.set_number(0, 0, "x")

def test_set_number_on_fixed_cell():
    grid = [[Number(0) for _ in range(9)] for _ in range(9)]
    grid[0][0] = Number(5, fixed=True)
    b = Board(grid)
    with pytest.raises(PermissionError):
        b.set_number(0, 0, 3)
    with pytest.raises(PermissionError):
        b.clear_number(0, 0)

# ----------------------------------------------------------------------
# METHOD allowed_numbers, is_valid
# ----------------------------------------------------------------------
def test_allowed_numbers():
    b = Board()
    b.set_number(0, 0, 1)
    b.set_number(0, 1, 2)
    b.set_number(1, 0, 3)
    allowed = b.allowed_numbers(0, 2)
    assert allowed is not None
    assert 1 not in allowed
    assert 2 not in allowed
    assert 3 not in allowed
    for n in allowed:
        assert 1 <= n <= 9

def test_is_valid():
    b = Board()
    b.set_number(0, 0, 1)
    assert not b.is_valid(0, 0)  # 1 already in row
    b.clear_number(0, 0)
    b.set_number(0, 1, 2)
    b.set_number(1, 0, 2)
    assert not b.is_valid(1, 0)  # 2 already in row

# ----------------------------------------------------------------------
# INTERNAL METHODS (PRIVATE)
# ----------------------------------------------------------------------
def test_internal_methods():
    b = Board()
    assert b._is_empty(0, 0)
    b.set_number(0, 0, 4)
    assert not b._is_empty(0, 0)
    assert b._get_row(0) == [4]
    assert b._get_column(0) == [4]
    assert b._get_subgrid(0, 0) == [4]

# ----------------------------------------------------------------------
# ROBUSTNESS OF MANIPULATIONS
# ----------------------------------------------------------------------
def test_manipulate_full_and_empty_board():
    b = Board()
    # Fill the entire grid
    for i in range(9):
        for j in range(9):
            b.set_number(i, j, ((i*9+j)%9)+1)
    for i in range(9):
        for j in range(9):
            val = b.get_number(i, j)
            assert val is not None
            assert 1 <= val <= 9
    # Clear the entire grid
    for i in range(9):
        for j in range(9):
            b.clear_number(i, j)
    for i in range(9):
        for j in range(9):
            assert b.get_number(i, j) == 0
""" Tests for the game module.
This module contains unit tests for the `Game` class in the Sudoku game.
"""
from core.game import Game
from core.board import Board
import pytest

# ----------------------------------------------------------------------
# METHOD __init__
# ----------------------------------------------------------------------
@pytest.mark.parametrize("level", ["easy", "medium", "hard", "expert"])
def test_init_valid_levels(level):
    g = Game(level)
    assert g.get_level() == level
    assert g.get_status() == "not started"
    assert isinstance(g.get_board(), Board)

def test_init_invalid_level():
    with pytest.raises(ValueError):
        Game("invalid")

# ----------------------------------------------------------------------
# METHOD set_level, get_level
# ----------------------------------------------------------------------
def test_set_get_level():
    g = Game("easy")
    g.set_level("hard")
    assert g.get_level() == "hard"
    with pytest.raises(ValueError):
        g.set_level("foo")

def test_set_get_status():
    g = Game("easy")
    g.set_status("in progress")
    assert g.get_status() == "in progress"
    with pytest.raises(ValueError):
        g.set_status("foo")

def test_set_get_board():
    g = Game("easy")
    b = Board()
    g.set_board(b)
    assert g.get_board() is b
    with pytest.raises(TypeError):
        g.set_board(123)

# ----------------------------------------------------------------------
# METHOD start_game
# ----------------------------------------------------------------------
def test_start_game_sets_status_and_fills_board():
    g = Game("easy")
    g.start_game()
    assert g.get_status() == "in progress"
    # The board must contain fixed numbers
    fixed_count = sum(g.get_board().get_number(i, j) != 0 for i in range(9) for j in range(9))
    assert fixed_count > 0

# ----------------------------------------------------------------------
# METHOD reset_game
# ----------------------------------------------------------------------
def test_reset_game_resets_board():
    g = Game("medium")
    g.start_game()
    old_board = g.get_board()
    g.reset_game()
    # The board must be different (new instance)
    assert g.get_board() is not old_board

# ----------------------------------------------------------------------
# METHOD end_game
# ----------------------------------------------------------------------
def test_end_game_completed(monkeypatch):
    g = Game("easy")
    g.start_game()
    # Monkeypatch _is_board_valid to simulate a win
    g._is_board_valid = lambda: True
    g.end_game()
    assert g.get_status() == "completed"

def test_end_game_not_completed(monkeypatch):
    g = Game("easy")
    g.start_game()
    g._is_board_valid = lambda: False
    g.end_game()
    assert g.get_status() == "in progress"

# ----------------------------------------------------------------------
# INTERNAL METHODS (PRIVATE)
# ----------------------------------------------------------------------
def test_clear_board():
    g = Game("easy")
    g.start_game()
    g._clear_board()
    assert all(g.get_board().get_number(i, j) == 0 for i in range(9) for j in range(9))

def test_is_board_valid_true():
    g = Game("easy")
    g.start_game()
    # Fill the grid with a valid solution
    for i in range(9):
        for j in range(9):
            g._board.set_number(i, j, ((i*3 + i//3 + j) % 9) + 1)
    assert g._is_board_valid() is True

def test_is_board_valid_false():
    g = Game("easy")
    g.start_game()
    # Put the same number twice in a row
    g._board.set_number(0, 0, 1)
    g._board.set_number(0, 1, 1)
    assert g._is_board_valid() is False

# ----------------------------------------------------------------------
# ROBUSTNESS AND ERRORS
# ----------------------------------------------------------------------
def test_set_board_typeerror():
    g = Game("easy")
    with pytest.raises(TypeError):
        g.set_board("not a board")

def test_set_status_valueerror():
    g = Game("easy")
    with pytest.raises(ValueError):
        g.set_status("invalid")

def test_set_level_valueerror():
    g = Game("easy")
    with pytest.raises(ValueError):
        g.set_level("invalid")

# ----------------------------------------------------------------------
# INTEGRATION (game lifecycle)
# ----------------------------------------------------------------------
def test_game_lifecycle():
    g = Game("medium")
    g.start_game()
    assert g.get_status() == "in progress"
    g.reset_game()
    assert g.get_status() == "in progress"
    g._is_board_valid = lambda: True
    g.end_game()
    assert g.get_status() == "completed"

# ----------------------------------------------------------------------
# EDGE CASES (end_game, reset_game without start)
# ----------------------------------------------------------------------
def test_end_game_without_start():
    g = Game("easy")
    g.end_game()
    assert g.get_status() == "not started"

def test_reset_game_without_start():
    g = Game("easy")
    g.reset_game()
    assert g.get_status() == "not started"
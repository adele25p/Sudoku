""" Core Module for Sudoku Game

This module provides classes and methods for managing the Sudoku board, numbers, and game logic.
They are essential for the functionality of the Sudoku game and are used by the CLI and GUI interfaces.

Structure:
    board.py     - Contains the Board class for grid management
    game.py      - Contains the Game class for game state and control
    number.py    - Contains the Number class for cell management
"""
from .game import Game

__all__ = ["Game"]

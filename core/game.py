""" Sudoku game class
This module is part of the core package of the Sudoku game.
It defines the `Game` class, which represents a Sudoku game and provides methods.
"""

from core.board import Board

class Game:
    """ Class representing a Sudoku game with methods for management and control. """

    def __init__(self, level):
        """ Initialize the Sudoku game by creating a new board and setting the game level.
        Args:
            level (str): The difficulty level of the Sudoku puzzle. Valid levels are "easy", "medium", "hard", and "expert".
        Raises:
            ValueError: If the level is not valid.
        """

    def __str__(self):
        """ Display the Sudoku game information.
        Returns:
            str: A string representation of the game.
        """
        return ""
    
    # Methods to manipulate the Sudoku game
    
    def get_level(self):
        """ Get the current level of the game.
        Returns:
            str: The difficulty level of the Sudoku puzzle.
        """

    def set_level(self, level):
        """ Set the difficulty level of the game.
            Delegates the check of the level to the `Board` class.
        Args:
            level (str): The new difficulty level of the Sudoku puzzle. Valid levels are "easy", "medium", "hard", and "expert".
        Raises:
            ValueError: If the level is not valid.
        """
    
    def get_board(self):
        """ Get the current board of the game.
        Returns:
            Board: The current board of the game.
        """

    def set_board(self, board):
        """ Set the current board of the game.
        Args:
            board (Board): The new board to set for the game.
        Raises:
            TypeError: If the board is not an instance of the Board class.
        """

    def start_game(self):
        """ Start the Sudoku game by filling the board with a valid Sudoku puzzle.
            Delegates the filling of the board to the '_fill_board' method.
        Returns:
            bool: True if the game was started successfully, False if there was an error in board initialization.
        Raises:
            RuntimeError: If the board could not be initialized with a valid Sudoku puzzle.
        """

    def reset_game(self):
        """ Reset the game by clearing the board and reinitializing it with a new valid Sudoku puzzle.
            Delegates the clearing of the board to the '_clear_board' method and the filling of the board to the '_fill_board' method.
        Returns:
            bool: True if the game was reset successfully, False if there was an error in board initialization.
        Raises:
            RuntimeError: If the board could not be reinitialized with a valid Sudoku puzzle.
        """

    def end_game(self):
        """ Check if the board is valid and complete, and if so, end the game.
        If the board is not complete or valid, it will not end the game.
            Delegates the validation of the board to the '_is_board_valid' method.
        Returns:
            bool: True if the game was ended successfully, False if there was an error in ending the game.
        """

    # Functions to support the above methods

    def _fill_board(self):
        """ Fill the current board with a valid Sudoku puzzle.
        Returns:
            bool: True if the board was filled successfully, False if there was an error.
        Raises:
            RuntimeError: If the board could not be filled with a valid Sudoku puzzle.
        """
    
    def _clear_board(self):
        """ Clear the current board by resetting all cells to empty.
        Returns:
            bool: True if the board was cleared successfully, False if there was an error.
        """

    def _is_board_valid(self):
        """ Check if the current board is valid (i.e., follows Sudoku rules).
        Returns:
            bool: True if the board is valid, False otherwise.
        """
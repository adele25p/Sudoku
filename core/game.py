""" Sudoku game class
This module is part of the core package of the Sudoku game.
It defines the `Game` class, which represents a Sudoku game and provides methods.
"""

from .board import Board

valid_levels = ["easy", "medium", "hard", "expert"]
statuses = ["not started", "in progress", "completed"]

class Game:
    """ Class representing a Sudoku game with methods for management and control. """

    def __init__(self, level):
        """ Initialize the Sudoku game by creating a new board and setting the game level.
        Args:
            level (str): The difficulty level of the Sudoku puzzle. Valid levels are "easy", "medium", "hard", and "expert".
        Raises:
            ValueError: If the level is not valid.
        """
        if level not in valid_levels:
            raise ValueError(f"Level must be one of {valid_levels}.")
        
        self._level = level
        self._board = Board()
        self._status = "not started"
        
    def __str__(self):
        """ Display the Sudoku game information.
        Returns:
            str: A string representation of the game.
        """
        return f"Sudoku Game - Level: {self._level}, Status: {self._status}\n{self._board}"
    
    # Methods to manipulate the Sudoku game
    
    def get_level(self):
        """ Get the current level of the game.
        Returns:
            str: The difficulty level of the Sudoku puzzle.
        """
        return self._level

    def set_level(self, level):
        """ Set the difficulty level of the game.
            Delegates the check of the level to the `Board` class.
        Args:
            level (str): The new difficulty level of the Sudoku puzzle. Valid levels are "easy", "medium", "hard", and "expert".
        Raises:
            ValueError: If the level is not valid.
        """
        if level not in valid_levels:
            raise ValueError(f"Level must be one of {valid_levels}.")
        self._level = level
    
    def get_board(self):
        """ Get the current board of the game.
        Returns:
            Board: The current board of the game.
        """
        return self._board

    def set_board(self, board):
        """ Set the current board of the game.
        Args:
            board (Board): The new board to set for the game.
        Raises:
            TypeError: If the board is not an instance of the Board class.
        """
        if not isinstance(board, Board):
            raise TypeError("Board must be an instance of the Board class.")
        self._board = board

    def get_status(self):
        """ Get the current status of the game.
        Returns:
            str: The current status of the game, which can be "not started", "in progress", or "completed".
        """
        return self._status
    
    def set_status(self, status):
        """ Set the current status of the game.
        Args:
            status (str): The new status of the game. Valid statuses are "not started", "in progress", and "completed".
        Raises:
            ValueError: If the status is not valid.
        """
        if status not in statuses:
            raise ValueError(f"Status must be one of {statuses}.")
        self._status = status

    def start_game(self):
        """ Start the Sudoku game by filling the board with a valid Sudoku puzzle.
            Delegates the filling of the board to the '_fill_board' method.
        Raises:
            RuntimeError: If the board could not be initialized with a valid Sudoku puzzle.
        """
        if not self._fill_board():
            raise RuntimeError("Could not initialize the board with a valid Sudoku puzzle.")
        self._status = "in progress"

    def reset_game(self):
        """ Reset the game by clearing the board and reinitializing it with a new valid Sudoku puzzle.
            Delegates the clearing of the board to the '_clear_board' method and the filling of the board to the '_fill_board' method.
        Raises:
            RuntimeError: If the board could not be reinitialized with a valid Sudoku puzzle.
        """
        if not self._fill_board():
            raise RuntimeError("Could not reinitialize the board with a valid Sudoku puzzle.")

    def end_game(self):
        """ Check if the board is valid and complete, and if so, end the game.
        If the board is not complete or valid, it will not end the game.
            Delegates the validation of the board to the '_is_board_valid' method.
        """
        if self._is_board_valid():
            self._status = "completed"

    # Functions to support the above methods

    def _fill_board(self):
        """ Fill the current board with a valid Sudoku puzzle.
        Returns:
            bool: True if the board was filled successfully, False if there was an error.
        Raises:
            RuntimeError: If the board could not be filled with a valid Sudoku puzzle.
        """
        pass
        # This method should call the Board class's method to fill the board with a valid Sudoku puzzle.

    def _clear_board(self):
        """ Clear the current board by replacing it with a new empty board. """
        self._board = Board()

    def _is_board_valid(self):
        """ Check if the current board is valid (i.e., follows Sudoku rules).
        Returns:
            bool: True if the board is valid, False otherwise.
        """
        for i in range(9):
            for j in range(9):
                if not self._board.is_valid(i, j):
                    return False
        return True
""" Sudoku Board Class
This module is part of the core package of the Sudoku game.
It defines the `Board` class, which represents a Sudoku board and provides methods for manipulation and validation.
"""

from core.number import Number

class Board:
    """ Class representing a Sudoku board with methods for manipulation and validation. """

    def __init__(self, grid=None, level="easy"):
        """ Initialize the Sudoku board with a given grid and level.
        Args:
            grid (list[list[Number]]): A 9x9 grid representing the Sudoku board where each cell is an instance of the Number class. Defaults to None, which initializes an empty board.
            level (str): The difficulty level of the Sudoku puzzle. Defaults to "easy". Valid levels are "easy", "medium", "hard", and "expert".
        Raises:
            ValueError: If the grid is not a 9x9 grid or if the level is not valid.
            TypeError: If the grid is not of the expected type (list[list[Number]]).
        """

    def __str__(self):
        """ Display the Sudoku board in a readable format.
        The zeroes in the grid are represented as dots (.) for better readability.
        Returns:
            str: A string representation of the Sudoku board, with rows and columns clearly delineated. (e.g., with spaces or newlines).
        """
        return ""
    
    # Methods to manipulate the Sudoku board

    def get_number(self, row, col):
        """ Get the number value at the specified row and column.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            int: The number at the specified position, or 0 if the cell is empty.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
        """

    def set_number(self, row, col, num):
        """ Set a number in the Sudoku board at the specified row and column.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
            Delegates the check of the number and its mutability to the `Number` class.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
            num (Number): The number to add (0-9). 0 represents an empty cell.
        Returns:
            bool: True if the number was added successfully, False if it violates Sudoku rules.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row, column, or number is not of the expected type (int).
            ValueError: If the number is not between 0 and 9.
            PermissionError: If the cell cannot be modified (e.g., if it is part of the initial grid).
        """

    def clear_number(self, row, col):
        """ Clear the number in the specified cell, setting it to zero.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
            Delegates the check of the cell mutability to the `Number` class.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            bool: True if the number was removed successfully, False if there was no number to remove (cell already empty).
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
            PermissionError: If the cell cannot be modified (e.g., if it is part of the initial grid).
        """

    def allowed_numbers(self, row, col):
        """ Get a list of numbers that can be placed in the specified cell without violating Sudoku rules.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
            Delegates the checks of cell mutability to the `Number` class.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            list[int]: A list of numbers that can be placed in the specified cell.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
            PersmissionError: If the cell cannot be modified (e.g., if it is part of the initial grid).
        """

    def is_valid(self, row, col):
        """ Check if the number at the specified row and column is valid according to Sudoku rules.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            bool: True if the number is valid, False otherwise.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
        """

    # Functions to support the above methods

    def _create_empty_grid(self):
        """ Create an empty 9x9 grid filled with Number instances initialized to zero.
        Returns:
            list[list[Number]]: A 9x9 grid where each cell is an instance of the Number class initialized
        """

    def _is_empty(self, row, col):
        """ Check if the specified cell is empty (contains zero).
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            bool: True if the cell is empty (contains zero), False otherwise.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
        """

    def _get_row(self, row):
        """ Get the numbers appearing in the specified row. Don't include zeroes.
            Delegates the check of the row index to the `_is_valid_row_col` method.
        Args:
            row (int): The row index (0-8).
        Returns:
            list[int]: A list of numbers from the specified row.
        Raises:
            IndexError: If the row index is out of bounds (not between 0 and 8).
            TypeError: If the row index is not of the expected type (int).
        """

    def _get_column(self, col):
        """ Get the numbers appearing in the specified column. Don't include zeroes.
            Delegates the check of the column index to the `_is_valid_row_col` method.
        Args:
            col (int): The column index (0-8).
        Returns:
            list[int]: A list of numbers from the specified column.
        Raises:
            IndexError: If the column index is out of bounds (not between 0 and 8).
            TypeError: If the column index is not of the expected type (int).
        """

    def _get_subgrid(self, row, col):
        """ Get the numbers appearing in the 3x3 subgrid containing the specified cell. Don't include zeroes.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            list[int]: A list of numbers from the specified 3x3 subgrid.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
        """

    def _is_valid_row_col(self, row, col):
        """ Check if the row and column indices are valid (between 0 and 8). And if they are of the expected type (int).
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Returns:
            bool: True if the row and column indices are valid, False otherwise.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
        """
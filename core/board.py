""" Sudoku Board Class
This module is part of the core package of the Sudoku game.
It defines the `Board` class, which represents a Sudoku board and provides methods for manipulation and validation.
"""

from core.number import Number

class Board:
    """ Class representing a Sudoku board with methods for manipulation and validation. """

    def __init__(self, grid=None):
        """ Initialize the Sudoku board with a given grid or an empty grid.
        Args:
            grid (list[list[Number]]): A 9x9 grid representing the Sudoku board where each cell is an instance of the Number class. Defaults to None, which initializes an empty board.
        Raises:
            ValueError: If the grid is not a 9x9 grid.
            TypeError: If the grid is not a list of lists containing Number instances.
        """
        if grid is None:
            self._grid = self._create_empty_grid()
        else:
            if len(grid) != 9 or any(len(row) != 9 for row in grid):
                raise ValueError("Grid must be a 9x9 grid.")
            if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid) or not all(isinstance(cell, Number) for row in grid for cell in row):
                raise TypeError("Grid must be a list of lists containing Number instances.")
            self._grid = grid

    def __str__(self):
        """ Display the Sudoku board in a readable format.
        Zeros in the grid are represented as dots (.) for better readability.
        Returns:
            str: A string representation of the Sudoku board, with rows and columns clearly delineated (e.g., with spaces or newlines).
        """
        board_str = ""
        for row in self._grid:
            row_str = " ".join(str(cell.get_value()) if cell.get_value() != 0 else '.' for cell in row)
            board_str += row_str + "\n"
        return board_str.strip()
    
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
        if self._is_valid_row_col(row, col):
            return self._grid[row][col].get_value()

    def set_number(self, row, col, num):
        """ Set a number in the Sudoku board at the specified row and column.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
            Delegates the check of the number and its mutability to the `Number` class.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
            num (Number): The number to add (0-9). 0 represents an empty cell.
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row, column, or number is not of the expected type (int).
            ValueError: If the number is not between 0 and 9.
            PermissionError: If the cell cannot be modified (e.g., if it is part of the initial grid).
        """
        if self._is_valid_row_col(row, col):
            self._grid[row][col].set_value(num)

    def clear_number(self, row, col):
        """ Clear the number in the specified cell, setting it to zero.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
            Delegates the check of the cell mutability to the `Number` class.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
            PermissionError: If the cell cannot be modified (e.g., if it is part of the initial grid).
        """
        if self._is_valid_row_col(row, col):
            self._grid[row][col].clear_value()

    def lock_number(self, row, col):
        """ Lock the number in the specified cell, making it immutable.
            Delegates the check of the row and column indices to the `_is_valid_row_col` method.
            Delegates the check of the cell mutability to the `Number` class.
        Args:
            row (int): The row index (0-8).
            col (int): The column index (0-8).
        Raises:
            IndexError: If the row or column index is out of bounds (not between 0 and 8).
            TypeError: If the row or column is not of the expected type (int).
            PermissionError: If the cell cannot be modified (e.g., if it is part of the initial grid).
        """
        if self._is_valid_row_col(row, col):
            self._grid[row][col].lock()

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
        row_numbers = self._get_row(row)
        col_numbers = self._get_column(col)
        subgrid_numbers = self._get_subgrid(row, col)
        if isinstance(row_numbers, list) and isinstance(col_numbers, list) and isinstance(subgrid_numbers, list):
            used_numbers = set(row_numbers + col_numbers + subgrid_numbers)
            return [num for num in range(1, 10) if num not in used_numbers]

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
        if self._is_valid_row_col(row, col):
            return self._grid[row][col].get_value() in self.allowed_numbers(row, col)

    # Functions to support the above methods

    def _create_empty_grid(self):
        """ Create an empty 9x9 grid filled with Number instances initialized to zero.
        Returns:
            list[list[Number]]: A 9x9 grid where each cell is an instance of the Number class initialized
        """
        return [[Number(0) for _ in range(9)] for _ in range(9)]

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
        if self._is_valid_row_col(row, col):
            return self._grid[row][col].get_value() == 0

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
        if self._is_valid_row_col(row, 0):
            return [self._grid[row][col].get_value() for col in range(9) if self._grid[row][col].get_value() != 0]

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
        if self._is_valid_row_col(0, col):
            return [self._grid[row][col].get_value() for row in range(9) if self._grid[row][col].get_value() != 0]

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
        if self._is_valid_row_col(row, col):
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            return [self._grid[r][c].get_value() for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3) if self._grid[r][c].get_value() != 0]

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
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError("Row and column indices must be integers.")
        if not (0 <= row < 9) or not (0 <= col < 9):
            raise IndexError("Row and column indices must be between 0 and 8.")
        return True
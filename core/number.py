""" Sudoku Number Class
This module is part of the core package of the Sudoku game.
It defines the `Number` class, which represents a number in a Sudoku cell and provides methods for manipulation.
"""

class Number:
    """ Class to represent a number with a value and a flag indicating if it is fixed. """

    def __init__(self, value=0, fixed=False):
        """ Initialize the number with a value and a flag indicating if it is fixed.
        Args:
            value (int): The value of the number (1-9). Default is 0, which represents an empty cell.
            fixed (bool): Whether the number is fixed (cannot be changed).
        Raises:
            ValueError: If the value is not between 0 and 9.
            TypeError: If the value is not of the expected type (int) or if fixed is not a boolean.
            PermissionError: If the number is initialized with a value of 0 and fixed is True.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        if not isinstance(fixed, bool):
            raise TypeError("Fixed must be a boolean.")
        
        self._value = value
        self._fixed = fixed

        if not self._is_valid():
            raise ValueError("Value must be between 0 and 9.")
        if self._value == 0 and self._fixed:
            raise PermissionError("Cannot initialize a fixed number with value 0 (empty cell).")

    def __str__(self):
        """ Return a string representation of the number.
        If the value is zero, it returns a dot (.) to represent an empty cell.
        Returns:
            str: The string representation of the number.
        """
        return str(self._value) if self._value != 0 else "."
    
    # Methods to manipulate the Number
    
    def get_value(self):
        """ Get the value of the number.
        Returns:
            int: The value of the number.
        """
        return self._value

    def set_value(self, value):
        """ Set the value of the number.
        Args:
            value (int): The new value of the number (1-9). 0 represents an empty cell.
        Raises:
            ValueError: If the value is not between 0 and 9.
            TypeError: If the value is not of the expected type (int).
            PermissionError: If the number is fixed and cannot be changed.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        if not (0 <= value <= 9):
            raise ValueError("Value must be between 0 and 9.")
        
        if self.is_fixed():
            raise PermissionError("Cannot change a fixed number.")
        
        self._value = value

    def clear_value(self):
        """ Clear the value of the number, setting it to zero.
        Raises:
            PermissionError: If the number is fixed and cannot be cleared.
        """
        if self.is_fixed():
            raise PermissionError("Cannot clear a fixed number.")
        
        self._value = 0

    def is_fixed(self):
        """ Check if the number is fixed (cannot be changed).
        Returns:
            bool: True if the number is fixed, False otherwise.
        """
        return self._fixed

    def lock(self):
        """ Lock the number, making it fixed (cannot be changed).
        Raises:
            PermissionError: If the number is already fixed or if the value is zero.
        """
        if self.is_fixed():
            raise PermissionError("Number is already fixed.")
        if self._value == 0:
            raise PermissionError("Cannot lock a number with value 0 (empty cell).")
        
        self._fixed = True

    # Methods to support the above methods

    def _is_valid(self):
        """ Check if the number is valid (value is between 0 and 9).
        Returns:
            bool: True if the number is valid, False otherwise.
        """
        return 0 <= self._value <= 9
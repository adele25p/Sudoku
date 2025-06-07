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
        """

    def __str__(self):
        """ Return a string representation of the number.
        Returns:
            str: The string representation of the number.
        """
        return ""
    
    # Methods to manipulate the Number
    
    def get_value(self):
        """ Get the value of the number.
        Returns:
            int: The value of the number.
        """

    def set_value(self, value):
        """ Set the value of the number.
        Args:
            value (int): The new value of the number (1-9). 0 represents an empty cell.
        Raises:
            ValueError: If the value is not between 0 and 9.
            TypeError: If the value is not of the expected type (int).
        """

    def clear_value(self):
        """ Clear the value of the number, setting it to zero.
        Raises:
            PermissionError: If the number is fixed and cannot be cleared.
        """

    def lock(self):
        """ Lock the number, making it fixed (cannot be changed).
        Raises:
            PermissionError: If the number is already fixed.
        """

    # Methods to support the above methods

    def _is_fixed(self):
        """ Check if the number is fixed (cannot be changed).
        Returns:
            bool: True if the number is fixed, False otherwise.
        """

    def _is_valid(self):
        """ Check if the number is valid (value is between 0 and 9).
        Returns:
            bool: True if the number is valid, False otherwise.
        """
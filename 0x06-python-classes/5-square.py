#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new square object.

        Args:
            size (int): size of the new square object.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the current square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the current squre object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the current square object."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

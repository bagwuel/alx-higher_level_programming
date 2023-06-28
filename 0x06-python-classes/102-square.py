#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square object.

        Args:
            size (int): The size of the new square object.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the current square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the current square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the current square object."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines >= compmarison to a Square."""
        return self.area() >= other.area()

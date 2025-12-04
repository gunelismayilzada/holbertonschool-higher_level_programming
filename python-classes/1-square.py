#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represents a square.
    
    Attributes:
        __size (int): The size of the square (private).
    """
    
    def __init__(self, size):
        """Initialize a new Square instance.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size

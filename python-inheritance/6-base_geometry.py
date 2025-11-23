#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def area(self):
        """
        Raise an exception for unimplemented area().
        """
        raise Exception("area() is not implemented")

#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for all animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog subclass of Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
    
#!/usr/bin/env python3

"""
File used to define attribute class and subclasses
"""

class Attribute():
    def __init__(value = 0):
        self.value = value


class Strength(Attribute):
    """
    Attribute used for attacks and brute strength interactions
    """
    def __init__(value = 0):
        super().__init__(value)

class Intelligence(Attribute):
    """
    Attribute used for magic and problem solving interactions
    """
    def __init__(value = 0):
        super().__init__(value)

class Charisma(Attribute):
    """
    Attribute used for speech interactions
    """
    def __init__(value = 0):
        super().__init__(value)

class Dexterity(Attribute):
    """
    Attribute used for speed and agility interactions
    """
    def __init__(value = 0):
        super().__init__(value)

class Defense(Attribute):
    """
    Attribute used for defense interactions
    """
    def __init__(value = 0):
        super().init(value)

class

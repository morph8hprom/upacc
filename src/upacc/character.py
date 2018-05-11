#!/usr/bin/env python3

"""
File used to define Character class and Player and Nonplayer subclasses
"""

class Character():
    def __init__(self, name, desc, attributes, armor, weapons):
        self.name = name
        self.desc = desc
        self.attributes = attributes
        self.armor = armor
        self.weapons = weapons



class Player(Character):
    def __init__(self, name, desc, attributes, armor, weapons):
        super().__init__(name, desc, attributes, armor, weapons)

    

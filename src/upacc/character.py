#!/usr/bin/env python3
from pkg_resources import resource_string
import json

"""
File used to define Character class and Player and Nonplayer subclasses
"""

class Character():
    def __init__(self, id = '1', name = 'test', desc = 'test desc',
                attributes = None, armor = None , weapons = None , player = True):
        self.id = id
        self.name = name
        self.desc = desc
        self.attributes = attributes
        self.armor = armor
        self.weapons = weapons
        self.player = player

    def __repr__(self):
        return "{}({}, {}, {}, {}, {}, {}, {})".format(self.__class__.__name__,
        self.id, self.name, self.desc, self.attributes, self.armor,
        self.weapons, self.player)



class Player(Character):
    def __init__(self, id, name, desc, attributes, armor, weapons, player, loc = None):
        super().__init__(id, name, desc, attributes, armor, weapons, player)
        self.loc = loc

class Nonplayer(Character):
    def __init__(self, id, name, desc, attributes, armor, weapons, player):
        super().__init__(id, name, desc, attributes, armor, weapons, player)

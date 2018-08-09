#!/usr/bin/env python3
from pkg_resources import resource_string
import json

"""
File used to define Character class and Player and Nonplayer subclasses
"""

class Character():
    def __init__(self, id = '1', name = 'test', desc = 'test desc',
                attributes = None, armor = None , weapons = None , player = True):
        self._id = id
        self._name = name
        self._desc = desc
        self._attributes = attributes
        self._armor = armor
        self._weapons = weapons
        self._player = player

    def __repr__(self):
        return "{}({}, {}, {}, {}, {}, {}, {})".format(self.__class__.__name__,
        self._id, self._name, self._desc, self._attributes, self._armor,
        self._weapons, self._player)



class Player(Character):
    def __init__(self, id = '1', name = 'test', desc = 'test desc',
                attributes = None, armor = None , weapons = None , player = True, loc = None):
        super().__init__(id, name, desc, attributes, armor, weapons, player)
        self._loc = loc

class Nonplayer(Character):
    def __init__(self, id = '1', name = 'test', desc = 'test desc',
                attributes = None, armor = None , weapons = None , player = False):
        super().__init__(id, name, desc, attributes, armor, weapons, player)

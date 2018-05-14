#!/usr/bin/env python3
from pkg_resources import resource_string
import json

"""
File used to define Character class and Player and Nonplayer subclasses
"""

class Character():
    def __init__(self, id, name, desc, attributes, armor, weapons, player ):
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
    def __init__(self, id, name, desc, attributes, armor, weapons, player):
        super().__init__(id, name, desc, attributes, armor, weapons, player)

class Nonplayer(Character):
    def __init__(self, id, name, desc, attributes, armor, weapons, player):
        super().__init__(id, name, desc, attributes, armor, weapons, player)




# def char_d(id, num_of_chars):
#     """
#     Create dictionary of characters from json files using build_char function
#     """
#     # Sets d as a an empty dictionary
#     d = {}
#
#     for i in range(id, num_of_chars + 1):
#         try:
#             d[i] = build_character(i)
#         except FileNotFoundError:
#             print('File not found.  Please check to make sure it exists')
#
#     return d
#
# def player_d(character_dict):
#     """
#     Takes character dictionary as argument and filters out only Player instances
#     """
#     d = {}
#     for i in character_dict.values():
#         if i.player is True:
#             d[i.id] = i
#     return d
#
# def nonplayer_d(character_dict):
#     """
#     Takes character dictionary as argument and filters out only Nonplayer instances
#     """
#     d = {}
#     for i in character_dict.values():
#         if i.player is False:
#             d[i.id] = i
#     return d

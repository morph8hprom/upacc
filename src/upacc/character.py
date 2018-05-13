#!/usr/bin/env python3
from pkg_resources import resource_string
import json

"""
File used to define Character class and Player and Nonplayer subclasses
"""

class Character():
    def __init__(self, name, desc, attributes, armor, weapons, player ):
        self.name = name
        self.desc = desc
        self.attributes = attributes
        self.armor = armor
        self.weapons = weapons
        self.player = player



class Player(Character):
    def __init__(self, id, name, desc, attributes, armor, weapons, player):
        super().__init__(name, desc, attributes, armor, weapons, player)

class Nonplayer(Character):
    def __init__(self, id, name, desc, attributes, armor, weapons, player):
        super().__init__(name, desc, attributes, armor, weapons, player)

def build_character(id):
    """
    Gathers character data from json file and returns Character instance.
    """

    jsontext = resource_string(__name__, 'data/char{}.json'.format(id))
    d = json.loads(jsontext.decode('utf-8'))
    d['id'] = id
    if d['player'] == False:
        char = Nonplayer(**d)
        return char
    elif d['player'] == True:
        char = Player(**d)
        return char
    else:
        raise ValueError('player key must be True or False')


def char_d(id, num_of_chars):
    """
    Create dictionary of characters from json files using build_char function
    """
    # Sets d as a an empty dictionary
    d = {}

    for i in range(id, num_of_chars + 1):
        try:
            d[i] = build_character(i)
        except FileNotFoundError:
            print('File not found.  Please check to make sure it exists')

    return d

def player_d(char_dict):
    """
    Takes character dict as argument and filters out only player characters
    """
    d = {}
    for i in char_dict.values():
        pass

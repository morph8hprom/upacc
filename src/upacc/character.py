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

class Nonplayer(Character):
    def __init__(self, name, desc, attributes, armor, weapons):
        super().__init__(name, desc, attributes, armor, weapons)

def build_character(id):
    """
    Gathers character data from json file and returns Character instance.
    """

    jsontext = resource_string(__name__, 'data/char{}.json'.format(id))
    d = json.loads(jsontext.decode('utf-8'))
    d['id'] = id
    if d['player'] == False:
        char = Nonplayer(**d)
    elif d['player'] == True:
        char = Player(**d)
    else:
        raise ValueError('player key must be True or False')

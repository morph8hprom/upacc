#!/usr/bin/env python3
from pkg_resources import resource_string
import json

"""
File used to define CharacterDict class and it's methods
"""

class CharacterDict():
    def __init__(self):
        self.all_chars = {}
        self.player_chars = {}
        self.nonplayer_chars = {}

    def __iter__:
        return iter(self.all_chars.items())

    def __len__(self):
        return len(self.all_chars)

    def __contains__(self, char):
        return char.id in self.all_chars

    def __getitem__(self, char):
        return self.all_chars[char.id]

    

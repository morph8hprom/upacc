#!/usr/bin/env python3
from pkg_resources import resource_string
import json

"""
File used to define CharacterDict class and it's methods
"""

class CharacterDict():
    def __init__(self, id = 1, num_of_chars = 2):
        # Dictionary containing reference to all characters
        self.all_chars = {}
        # Dictionary containing reference to only player characters
        self.player_chars = {}
        # Dictonary containing reference to only nonplayer characters
        self.nonplayer_chars = {}

        self._id = id
        self._num_of_chars = num_of_chars

    # def __repr__(self):
    #     repr = {}
    #     for i in self.all_chars.values():
    #         repr['id'] = i.id
    #         repr['name'] = i.name
    #         repr['player'] = i.player
    #     # return '{}'.format(.join([x, a for x, a in ]))


    def __iter__(self):
        return iter(self.all_chars.items())

    def __len__(self):
        return len(self.all_chars)

    def __contains__(self, char):
        return char.id in self.all_chars

    def __getitem__(self, char):
        return self.all_chars[char.id]

    def _build_character(id):
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


    def _update_main_dict(self):
        for i in range(self._id, self._num_of_chars):
            try:
                d[i] = _build_character(i)
            except FileNotFoundError:
                print('File not found.  Please check to make sure it exists')

        self.all_chars = d


    def _update_secondary_dicts(self):
        for i in self.all_chars.values():
            if i.player == True:
                self.player_chars[i.id] = i
            elif i.player == False:
                self.nonplayer_chars[i.id] = i
            else:
                raise ValueError('player key must be True or False')

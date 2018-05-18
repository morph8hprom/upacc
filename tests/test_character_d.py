#!/usr/bin/env python3

import unittest
import json
from gim import item
from upacc import character_dict as ch_d

class CharacterDictAttributeTestCase(unittest.TestCase):
    """
    Contains tests for CharacterDict instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of CharacterDict
        """
        cls.test_char_d = ch_d.CharacterDict()

    def test_char_d_has_all_chars(self):
        att = hasattr(self.test_char_d, 'all_chars')
        self.assertTrue(att)

    def test_char_d_has_player_chars(self):
        att = hasattr(self.test_char_d, 'player_chars')
        self.assertTrue(att)

    def test_char_d_has_nonplayer_chars(self):
        att = hasattr(self.test_char_d, 'nonplayer_chars')
        self.assertTrue(att)

class CharacterDictMethodTestCase(unittest.TestCase):
    pass

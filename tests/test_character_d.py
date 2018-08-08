#!/usr/bin/env python3

import unittest
import json
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
    """
    Contains tests for CharacterDict methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of ChracterDict
        """
        cls.test_char_d = ch_d.CharacterDict()


    def test_build_char_method_for_player(self):
        # Assumes that character data file with char_id has the attribute player = True
        # if it does not, change char_id to a file which does

        char_id = 1
        test_char = self.test_char_d._build_character(char_id)
        att = isinstance(test_char, ch_d.ch.Player)
        self.assertTrue(att)

    def test_build_char_method_for_nonplayer(self):
        # Assumes that character data file with char_id has the attribute player = False
        # if it does not, change char_id to a file which does

        char_id = 2
        test_char = self.test_char_d._build_character(char_id)
        att = isinstance(test_char, ch_d.ch.Nonplayer)
        self.assertTrue(att)




    def test_update_main_dict(self):
        self.test_char_d._num_of_chars = 3
        pre_update = len(self.test_char_d.all_chars)
        self.test_char_d._update_main_dict()
        post_update = len(self.test_char_d.all_chars)
        self.assertNotEqual(pre_update, post_update)

    def test_update_secondary_dicts_player(self):
        test_char = ch_d.ch.Character(player = True)
        self.test_char_d.all_chars[test_char._id] = test_char
        pre_update = len(self.test_char_d.player_chars)
        self.test_char_d._update_secondary_dicts()
        post_update = len(self.test_char_d.player_chars)
        self.assertNotEqual(pre_update, post_update)


    def test_update_secondary_dicts_nonplayer(self):
        test_char = ch_d.ch.Character(player = False)
        self.test_char_d.all_chars[test_char._id] = test_char
        pre_update = len(self.test_char_d.nonplayer_chars)
        self.test_char_d._update_secondary_dicts()
        post_update = len(self.test_char_d.nonplayer_chars)
        self.assertNotEqual(pre_update, post_update)

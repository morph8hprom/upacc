#!/usr/bin/env python3

import unittest
from upacc import character as ch


class CharacterAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Character instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of Character using default parameters
        """
        cls.test_char = ch.Character()

    def test_character_has_id(self):
        att = hasattr(self.test_char, '_id')
        self.assertTrue(att)

    def test_character_has_name(self):
        att = hasattr(self.test_char, '_name')
        self.assertTrue(att)

    def test_character_has_desc(self):
        att = hasattr(self.test_char, '_desc')
        self.assertTrue(att)

    def test_character_has_attributes(self):
        att = hasattr(self.test_char, '_attributes')
        self.assertTrue(att)

    def test_character_has_armor(self):
        att = hasattr(self.test_char, '_armor')
        self.assertTrue(att)

    def test_character_has_weapons(self):
        att = hasattr(self.test_char, '_weapons')
        self.assertTrue(att)

    def test_character_has_player(self):
        att = hasattr(self.test_char, '_player')
        self.assertTrue(att)

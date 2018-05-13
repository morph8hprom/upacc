#!/usr/bin/env python3

import unittest
import json
from gim import item
from uapcc import character
from upacc import inventory

class CharacterAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Character instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds dictionary of all characters stores in data folder
        Builds item dictionaries
        """
        

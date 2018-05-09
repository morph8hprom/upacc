#!/usr/bin/env python3

import unittest
from src.attrib import *

class AttribMethodsTestCase(unittest.TestCase):
    """
    Contains test for Attrib instance methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Uses the build_attrib_list function to create an instance of
        the Attriblist class and the various instances for each individual subclass
        """

        cls.attrib_list = build_attrib_list()

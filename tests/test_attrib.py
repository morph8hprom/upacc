#!/usr/bin/env python3
import unittest
from upacc import attrib

class AttribAttributesTestCase(unittest.TestCase):
    """
    Containst test for Attrib instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Uses the build_attrib_list function to create an instance of
        the Attriblist class and the various instances for each individual subclass
        """

        cls.attrib_list = attrib.build_attrib_list()
        cls.attribs = cls.attrib_list.attributes.values()

    def test_attribs_have_value(self):
        for i in self.attribs:
            att = hasattr(i ,'value')
            self.assertTrue(att)


class AttribMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Attrib instance methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Uses the build_attrib_list function to create an instance of
        the Attriblist class and the various instances for each individual subclass
        """

        cls.attrib_list = attrib.build_attrib_list()

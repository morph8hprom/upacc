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
            att = hasattr(i ,'_value')
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
        cls.attribs = cls.attrib_list.attributes.values()

    def test_attrib_list_is_iterable(self):
        try:
            iter(self.attrib_list)
            att = True
        except TypeError:
            att = False
        self.assertTrue(att)

    def test_attrib_list_len_returns_correct_number(self):
        all_subs_len = len(attrib.Attrib.__subclasses__())
        att_list_len = len(self.attrib_list)
        if all_subs_len > 0:
            self.assertEqual(all_subs_len, att_list_len)
        else:
            raise ValueError

    def test_attrib_list_contains_method(self):
        for i in self.attribs:
            att = i in self.attrib_list
            self.assertTrue(att)

    def test_attribute_getitem(self):
        pass

    def test_setitem(self):
        val = 10
        for i in self.attribs:
            self.attrib_list[i._name] = val
            att = self.attrib_list[i._name].value
            self.assertEqual(val, att)

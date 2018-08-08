#!/usr/bin/env python3

import unittest
import json
from gim import item as I
from upacc import inventory as inv


class InventoryAttributesTestCase(unittest.TestCase):
    """
    Contains test for Inventory instance attributes
    """

    @classmethod
    def setUpClass(cls):
        cls.test_inventory = inv.Inventory()

    def test_inventory_has_items(self):
        att = hasattr(self.test_inventory, 'items')
        self.assertTrue(att)

class InventoryMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Inventory instance methods
    """

    @classmethod
    def setUpClass(cls):
        cls.test_inventory = inv.Inventory()
        cls.test_item = I.Item()
        cls.test_item_2 = I.Item(3)

    def test_add_item(self):
        self.test_inventory._add_item(self.test_item)
        att = self.test_inventory[self.test_item]
        self.assertEqual(att, self.test_item)

    def test_drop_item(self):
        self.test_inventory._add_item(self.test_item_2)
        pre_drop = len(self.test_inventory)
        self.test_inventory._drop_item(self.test_item)
        post_drop = len(self.test_inventory)
        self.assertNotEqual(pre_drop, post_drop)

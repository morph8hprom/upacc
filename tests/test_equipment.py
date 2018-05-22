#!/usr/bin/env python3

import unittest
from upacc import equipment as eq
from gim import item as I

class EquipmentAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Equipment instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of Equipment
        """
        cls.test_equip = eq.Equipment()

    def test_equipment_has_slots(self):
        att = hasattr(self.test_equip, 'slots')
        self.assertTrue

class ArmorAttributesTestCase(unittest.TestCase):
    """
    Contains tests for Armor subclass instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of Armor
        """
        cls.test_armor = eq.Armor()

    def test_armor_has_slots(self):
        att = hasattr(self.test_armor, 'slots')
        self.assertTrue(att)

class ArmorMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Armor subclass instance methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds test instance of eq.Armor and test instance of I.Armor
        """
        cls.test_armor_eq = eq.Armor()
        cls.test_armor_item = I.Armor(slot = 'head')

    def test_armor_equip_method(self):
        self.test_armor_eq._equip_item(self.test_armor_item)
        att = self.test_armor_eq[self.test_armor_item]
        self.assertEqual(att, self.test_armor_item)

class WeaponsAttributeTestCase(unittest.TestCase):
    """
    Contains tests for Weapons subclass instance attributes
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of Weapons
        """
        cls.test_weapons = eq.Weapons()

    def test_weapons_has_slots(self):
        att = hasattr(self.test_weapons, 'slots')
        self.assertTrue(att)

class WeaponsMethodsTestCase(unittest.TestCase):
    """
    Contains tests for Weapons subclass instance methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Builds a test instance of eq.Weapons and two test instances of I.Weapon
        """
        cls.test_weapons_eq = eq.Weapons()
        cls.test_weapon_one = I.Weapon()
        cls.test_weapon_two = I.Weapon(two_handed = True)

    def test_equip_weapon_one_handed(self):
        self.test_weapons_eq._equip_item(self.test_weapon_one)
        att = self.test_weapons_eq[self.test_weapon_one]
        self.assertEqual(att, self.test_weapon_one)

    def test_equip_two_handed(self):
        self.test_weapons_eq._equip_item(self.test_weapon_two)
        att = self.test_weapons_eq[self.test_weapon_two]
        self.assertEqual(att, self.test_weapon_two)

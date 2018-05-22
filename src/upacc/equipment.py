#!/usr/bin/env python3

"""
File used to define equipment class, armor and weapon subclasses,
and related methods
"""

class Equipment:
    """
    Attributes and method for the Equipment class
    """

    def __init__(self):
        self.slots = {}

    def __iter__(self):
        # Defines item as an iterable
        return iter(self.slots.items())

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        # Overwrites __contains__ method for easy use of 'if x in items'
        return item in self.slots.values()

    def __getitem__(self, item):
        # Overwrites __getitem__ method for easy access to individual items
        return self.slots[item._slot]






class Armor(Equipment):
    """
    Attributes and methods for the Armor subclass
    """

    def __init__(self):
        self.slots = {'head' : None,
        'torso' : None,
        'arms' : None,
        'legs' : None,
        'feet' : None}

    def _equip_item(self, item):
        # Checks to make sure that the slot attribute of the item
        # is a valid available slot
        if item._slot in self.slots.keys():
            self.slots[item._slot] = item

        else:
            raise KeyError('Invalid slot')

class Weapons(Equipment):
    """
    Attributes and methords for the Weapons subclass
    """

    def __init__(self):
        self.slots = {'left' : None, 'right' : None}

    def _equip_item(self, item, slot = 'left'):
        if item.two_handed == False:
            try:
                self.slots[slot] = item
                item._slot = slot
            except KeyError:
                print("Slot must be left or right")
        else:
            self.slots['left'] = self.slots['right'] = item
            item._slot = slot

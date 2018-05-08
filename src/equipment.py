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
        return self.slots[item.slot]


    def _equip_item(self, item):
        # Checks to make sure that the slot attribute of the item
        # is a valid available slot
        if item.slot in self.slots.keys():
            self.slots[item.slot] = item

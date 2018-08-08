#!/usr/bin/env python3


"""
File used to define inventory class and related methods
"""

class Inventory():
    """
    Attributes and methods for the base Inventory class
    """

    def __init__(self):
        self.items = {}

    def __iter__(self):
        # Defines item as an iterable
        return iter(self.items.items())

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        # Overwrites __contains__ method for easy use of 'if x in items'
        return item._id in self.items

    def __getitem__(self, item):
        # Overwrites __getitem__ method for easy access to individual items
        return self.items[item._id]['item']

    def _get_quant(self, item):
        # Returns the quantity of item
        quant  = self.items[item._id]['quant']
        return quant

    def _add_item(self, item):
        # Adds item to inventory
        if item._id not in self.items:
            self.items[item._id] = {}
            self.items[item._id]['item'] = item
            self.items[item._id]['quant'] = 1
        else:
            self.items[item._id]['quant'] += 1


    def _drop_item(self, item):
        # Checks that the quantity is 1
        if self.items[item._id]['quant'] == 1:
            try:
                del self.items[item._id]
            except KeyError:
                print("Item not in inventory")
        elif self.items[item._id]['quant'] >= 2:
            self.items[item._id]['quant'] -= 1
        else:
            raise KeyError('Item not in inventory')

#!/usr/bin/env python3

"""
File used to define equipment class and related methods
"""

class Equipment:
    """
    Attributes and method for the Equipment class
    """

    def __init__(self):
        self.slots = {'head' : None, 'torso' : None, 'arms' : None,
                     'legs' : None}
    def __iter__(self):
        # Defines item as an iterable
        return iter(self.slots.items())

    def __len__(self):
        return len(self.slots)
    

#!/usr/bin/env python3

"""
File used to define class for non player character
"""
class Character():
    def __init__(name, desc, attributes = {}, equipment = {}):
        self.name = name
        self.desc = desc
        self.attributes = attributes
        self.equipment = equipment

    

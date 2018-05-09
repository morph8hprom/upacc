#!/usr/bin/env python3

"""
File used to define attribute class and subclasses
"""

class Attrib():
    def __init__(self, value = 0):
        self.value = value


class Strength(Attrib):
    """
    Attrib used for attacks and brute strength interactions
    """
    _name = 'Strength'
    def __init__(self, value = 0):
        super().__init__(value)

class Intelligence(Attrib):
    """
    Attrib used for magic and problem solving interactions
    """
    _name = 'Intelligence'
    def __init__(self, value = 0):

        super().__init__(value)

class Charisma(Attrib):
    """
    Attrib used for speech interactions
    """
    _name = 'Charisma'
    def __init__(self, value = 0):

        super().__init__(value)

class Dexterity(Attrib):
    """
    Attrib used for speed and agility interactions
    """
    _name = 'Dexterity'
    def __init__(self, value = 0):

        super().__init__(value)

class Defense(Attrib):
    """
    Attrib used for defense interactions
    """
    _name = 'Defense'
    def __init__(self, value = 0):
        self.name = 'Defense'
        super().__init__(value)

class Attriblist:

    def __init__(self):
        self.attributes = {}

    def __iter__(self):
        return iter(self.attributes.items())

    def __len__(self):
        return len(self.attributes)

    def __contains__(self, attrib):
        return attrib in self.attributes.values()

    def __getitem__(self, attrib):
        return self.attributes[attrib]

    def __setitem__(self, attrib, num):
        try:
            self.attributes[attrib].value = num
        except TypeError:
            print("Value must be integer")








def build_attrib_list():
    attrib_list = Attriblist()
    for i in Attrib.__subclasses__():
        attrib_list.attributes[i._name] = i()
    return attrib_list


if __name__ == '__main__':
    print(Attrib.__subclasses__())
    attrib_list = build_attrib_list()

    print(attrib_list['Strength'].value)
    attrib_list['Strength'] = 10
    print(attrib_list['Strength']._name)
    print(attrib_list['Strength'].value)

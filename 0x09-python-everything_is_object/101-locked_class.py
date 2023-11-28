#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("You cannot add new attributes to LockedClass")
        self.__dict__[name] = value

#!/usr/bin/python3

"""Defines an object attribute lookup funtion."""


def lookup(obj):
    """Return a list of an objects's avaliable attributes."""
    return dir(obj)

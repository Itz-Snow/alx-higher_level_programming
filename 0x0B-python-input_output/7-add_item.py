#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    try:
        """ Try to load existing data from the file"""
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        """ If the file doesn't exist, start with an empty list"""
        items = []

    """ Add command-line arguments to the list"""
    items.extend(sys.argv[1:])

    """ Save the updated list to the file """
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()

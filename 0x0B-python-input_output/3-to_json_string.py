#!/usr/bin/python3
"""Module 3-write_file.
Writes in a text file.
"""


import json


def to_json_string(my_obj):
    """Returns th JSON representation of my_obj.

    Args:
        - my_obj: string to represent

    Returns: JSON representation
    """

    return json.dumps(my_obj)

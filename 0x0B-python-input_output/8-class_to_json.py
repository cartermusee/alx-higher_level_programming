#!/us/bin/python3
"""module for clss to json"""


def class_to_json(obj):
    """function to class json return"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}

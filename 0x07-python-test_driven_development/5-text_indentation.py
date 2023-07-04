#!/usr/bin/python3

"""a module string and text identation"""


def text_indentation(text):

    """a function that idents text
    
    args:
        text:the text itself
    returns nothing
    raise:
        a typerror if not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    character = ['.', '?', ':']
    lines = []
    current = ""

    for char in text:
        current += char
        if char in character:
            lines.append(current.strip())
            lines.append("\n")
            current = ""
    lines.append(current.split())
    print("\n".join(lines))

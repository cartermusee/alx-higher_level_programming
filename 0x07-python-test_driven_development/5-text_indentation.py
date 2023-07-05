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

    cp = text[:]
    char = ['.', '?', ':']

    for y in char:
        list_of_text = cp.split(y)
        cp = ""
        for j in list_of_text:
            j = j.strip(" ")
            cp = j + y if cp is "" else cp + "\n\n" + j + y

    print(cp[:-3], end="")

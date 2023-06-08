#!/usr/bin/python3
if __name__ == "__main__":
    """all names defined by hidden module."""

    import hidden_4

    nm = dir(hidden_4)
    for i in nm:
        if name[:2] != "__":
            print(nm)

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    ln = len(my_list) - 1
    if idx > ln:
        return None
    for i in range(ln):
        my_list[i] = idx + 1
    return my_list[i]

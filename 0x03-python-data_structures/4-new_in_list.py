#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    my_new = my_list.copy()
    my_new[idx] = element
    return my_new

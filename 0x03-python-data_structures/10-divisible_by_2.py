#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    len_my_list = len(my_list)
    if len_my_list == 0:
        return None
    new_list = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            new_list.append(true)
        else:
            new_list.append(false)

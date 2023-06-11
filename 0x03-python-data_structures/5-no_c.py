#!/usr/bin/python3
def no_c(my_string):
    ln = len(my_string) - 1
    new = ""
    for i in range(ln):
        if my_string[i] != 'c' and  my_string[i] != 'C':
            new += my_string[i]
    return new 

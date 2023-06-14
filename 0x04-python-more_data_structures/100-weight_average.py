#!/usr/bin/python3
def weight_average(my_list=[]):
    ave = 0
    div = 0
    for i in my_list:
        ave += i[0] * i[1]
    return float(ave / div)

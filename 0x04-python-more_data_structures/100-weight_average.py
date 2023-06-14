#!/usr/bin/python3
def weight_average(my_list=[]):
    my_sum = 0
    wsum = 0
    if len(my_list) == 0:
        return (0)
    for x in my_list:
        wsum += (x[0] * x[1])
        my_sum += x[1]
    return (wsum / my_sum)

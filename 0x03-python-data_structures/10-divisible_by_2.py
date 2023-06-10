#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        return ([x % 2 == 0 for x in my_list])

#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0
    my_list = list(a_dictionary.keys())
    for x in my_list:
        sum += 1
    return (sum)

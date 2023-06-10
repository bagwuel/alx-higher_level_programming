#!/usr/bin/python3
def no_c(my_string):
    new_str = [x for x in my_string if x.lower() != "c"]
    return ("".join(new_str))

#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    max = my_list[0]
    if length == 0:
        return (None)
    else:
        for i in range(length - 1):
            if max < my_list[i + 1]:
                max = my_list[i + 1]
    return (max)

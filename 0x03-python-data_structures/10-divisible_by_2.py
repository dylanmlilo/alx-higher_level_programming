#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples[i] = True
        else:
            multiples[i] = False
    return (multiples)

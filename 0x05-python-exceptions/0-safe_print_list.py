#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in my_list:
            if (n < x):
                print("{:d}".format(i), end='')
                n += 1
        print('')
    except TypeError:
        pass
    finally:
        return n

#!/usr/bin/python3
import calculator_1
a = 10
b = 5
addition = calculator_1.add(a, b)
subtraction = calculator_1.sub(a, b)
multiplication = calculator_1.mul(a, b)
division = calculator_1.div(a, b)
print("{} + {} = {}".format(a, b, addition))
print("{} - {} = {}".format(a, b, subtraction))
print("{} * {} = {}".format(a, b, multiplication))
print("{} / {} = {}".format(a, b, division))

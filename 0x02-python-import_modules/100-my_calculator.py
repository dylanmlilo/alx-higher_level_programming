#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        operator = '+'
        result = add(a, b)
    elif sys.argv[2] == '-':
        operator = '-'
        result = sub(a, b)
    elif sys.argv == '*':
        operator = '*'
        result = mul(a, b)
    elif sys.argv == '/':
        operator = '/'
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {operator} {b} = {result}")

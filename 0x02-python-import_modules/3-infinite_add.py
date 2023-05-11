#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv)
    total = 0
    for i in range(1, args):
        total = total + int(sys.argv[i])
    print(total)

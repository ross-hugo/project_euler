#!/usr/bin/python
import sys
import math

def lcm(ceil):
    num = 1
    for i in range(2, ceil):
        num = int((num * i) / math.gcd(num, i))
    return num

def main():
    num = 20
    if len(sys.argv) != 1:
        num = int(sys.argv[1])
    print(lcm(num))

if __name__ == "__main__":
    main()

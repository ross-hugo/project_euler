#!/usr/bin/env python
import sys

def sum_mult_3_5(ceiling):
    return sum([x for x in range(ceiling) if x % 3 == 0 or x % 5 == 0])

def main():
    num = 1000
    if len(sys.argv) != 1: 
        num = int(sys.argv[1])
    print(sum_mult_3_5(num))

if __name__ == "__main__":
    main()

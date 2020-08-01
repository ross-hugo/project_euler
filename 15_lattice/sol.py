#!/usr/bin/python
import sys
import math

def get_paths(n, m):
    return math.comb(2*n, m)

def main():
    n, m = 20, 20
    if len(sys.argv) != 1:
        n, m = int(sys.argv[1]), int(sys.argv[2])
    print(get_paths(n, m))

if __name__ == "__main__":
    main()


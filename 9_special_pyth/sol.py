#!/usr/bin/python
import sys
import math

def is_square(n):
    return n == math.isqrt(n) ** 2

def find(num):
    for i in range(1, num//3 + 1):
        for j in range(i + 1, (num * 2) // 3):
            c = num - i - j 
            if i*i + j*j == c*c:
                return i * j * c

def main():
    n = 1000
    if len(sys.argv) != 1:
        n = int(sys.argv[1])
    print(find(n))

if __name__ == "__main__":
    main()


#!/usr/bin/python
import sys

def is_palin(num):
    num_str = str(num)
    for i in range(len(num_str)//2):
        if num_str[i] != num_str[len(num_str) - 1 - i]:
            return False
    return True

def lar_palin(digits):
    #these optimizations were bad i know but eh TODO ig
    max_ = int("1" + "0"*digits) - 1
    min_ = int("1" + "0"*(digits - 1))
    large_pal = 0
    for i in range(max_, min_, -1):
        for j in range(i, min_, -1):
            if i % 11 == 0 or j % 11 == 0:
                if is_palin(i*j) and i*j > large_pal:
                    large_pal = i*j
    return large_pal

def main():
    dig = 3
    if len(sys.argv) != 1:
        dig = int(sys.argv[1])
    print(lar_palin(dig))

if __name__ == "__main__":
    main()

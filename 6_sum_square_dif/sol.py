#!/usr/bin/python
import sys

def sum_dif(num):
    #just use math formulas
    return int(((num * (num + 1)) /2)**2 - ((num * (num + 1) * (2 * num + 1))/6))
def main():
    n = 100
    if len(sys.argv) != 1:
        n = int(sys.argv[1])
    print(sum_dif(n))

if __name__ == "__main__":
    main()

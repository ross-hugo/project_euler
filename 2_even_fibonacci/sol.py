#!/usr/bin/python
import sys


def even_fib(ceil):
    fir = 1
    sec = 1
    thir = 2
    even_fib = []
    while True:
        if thir > ceil:
            break
        if thir % 2 == 0:
            even_fib.append(thir)
        fir = sec
        sec = thir
        thir = fir + sec
    return sum(even_fib)

def main():
    num = 4000000
    if len(sys.argv) != 1:
        num = int(sys.argv[1])
    print(even_fib(num))

if __name__ == "__main__":
    main()

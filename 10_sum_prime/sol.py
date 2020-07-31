#!/usr/bin/python
import sys

def sieve(n):
    primes = [True for _ in range(n+1)]
    print('hi')
    for i in range(2, n//2):
        if primes[i]:
            print(i)
            for j in range(i*i, n+1, i):
                primes[j] = False
    return int(sum([ i for i in range(len(primes)) if primes[i]])) - 1

def main():
    n = 2000000
    if len(sys.argv) != 1:
        n = int(sys.argv[1])
    print(sieve(n))

if __name__ == "__main__":
    main()

#!/usr/bin/python
import sys
from random import randrange

def large_prime_fac(n):
    #TODO optimize this cuz kinda slow
    #TODO try this using rho algorithm
    primes = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = True
            for prime in primes:
                if i % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(i)
    return primes[-1]


def main():
    num = 600851475143
    if len(sys.argv) != 1:
        num = int(sys.argv[1])
    print(large_prime_fac(num))

if __name__ == "__main__":
    main()

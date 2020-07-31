#!/usr/bin/python
import sys

def num_primes(n):
    primes = [2]
    i = 3
    while True:
        if len(primes) >= 10001:
            break
        add_prime = True
        for prime in primes:
            if i % prime == 0:
                add_prime = False
        if add_prime:
            primes.append(i)
        i += 2
    return primes[10000]


def main():
    num = 10001
    if len(sys.argv) != 1:
        num = int(sys.argv[1])
    print(num_primes(num))

if __name__ == "__main__":
    main()

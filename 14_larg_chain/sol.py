#!/usr/bin/python
import sys

def long_chain(n):
    max_chain = 0
    max_val = 0
    for i in range(2, n):
        temp = i 
        temp_count = 1
        while temp != 1:
            if n % 2 == 0:
                temp = int(temp / 2)
            else:
                temp = int(3 * temp + 1)
            temp_count += 1
        if temp_count > max_chain:
            max_chain = temp_count
            max_val = i
    return max_val

def main():
    num = 1000000
    if len(sys.argv) != 1:
        num = int(sys.argv[1])

    print(long_chain(num))

if __name__ == "__main__":
    main()

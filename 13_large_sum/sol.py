#!/bin/usr/python
import sys

def find_10_sum(arr):
    big_sum = sum(arr)
    return int(str(big_sum)[:10])
def main():
    filename = "input.txt"
    if len(sys.argv) != 1:
        filename = sys.argv[1]
    mat = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines: 
            mat.append(int(line))
    print(find_10_sum(mat))

if __name__ == "__main__":
    main()
        

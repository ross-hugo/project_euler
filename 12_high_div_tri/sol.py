#!?usr/bin/python
import sys

def tri_num_div(num):
    tri = 1
    while True:
        if tri != 1 and len(tri_divisors) >= num:
            print(tri_divisors)
            return expanded
        tri_divisors = []
        expanded = tri * (tri + 1) // 2
        for i in range(1, int(expanded ** 0.5)):
            if expanded % i == 0:
                tri_divisors.append(i)
                tri_divisors.append(expanded//i)

        tri += 1

def main():
    n = 500 
    if len(sys.argv) != 1:
        n = sys.argv[1]
    print(tri_num_div(n))

if __name__ == "__main__":
    main()

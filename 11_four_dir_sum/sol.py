#!/usr/bin/python
import sys

def mat_up_down(matrix):
    max_num = 0
    for i in range(len(matrix) - 4):
        for j in range(len(matrix[i])):
            num = matrix[i][j] * \
                    matrix[i+1][j] * \
                    matrix[i+2][j] * \
                    matrix[i+3][j]
            max_num = max(max_num, num)
    return max_num

def mat_r_l(matrix):
    max_num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 4):
            num = matrix[i][j] * \
                    matrix[i][j + 1] * \
                    matrix[i][j + 2] * \
                    matrix[i][j + 3]
            max_num = max(max_num, num)
    return max_num

def mat_r_diag(matrix):
    max_num = 0
    for i in range(len(matrix) - 4):
        for j in range(len(matrix[i]) - 4):
            num = matrix[i][j] * \
                    matrix[i + 1][j + 1] * \
                    matrix[i + 2][j + 2] * \
                    matrix[i + 3][j + 3]
            max_num = max(max_num, num)
    return max_num

def mat_l_diag(matrix):
    max_num = 0
    for i in range(len(matrix) - 4):
        for j in range(3, len(matrix[i])):
            num = matrix[i][j] * \
                    matrix[i + 1][j - 1] * \
                    matrix[i + 2][j - 2] * \
                    matrix[i + 3][j - 3]
            max_num = max(max_num, num)
    return max_num

def find_max(mat):
    return max(mat_up_down(mat), mat_r_l(mat), mat_r_diag(mat), mat_l_diag(mat))


def main():
    filename = "input.txt"
    if len(sys.argv) != 1:
        filename = sys.argv[1]
    arg_mat = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            arg_mat.append([int(num) for num in line.split(' ')])
    print(find_max(arg_mat))

if __name__ == "__main__":
    main()

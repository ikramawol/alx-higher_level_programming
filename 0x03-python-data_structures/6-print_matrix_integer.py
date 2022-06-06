#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    spc = " "
    for submatrix in matrix:
        print(spc.join("{:d}".format(i) for i in submatrix))

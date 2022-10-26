#!/usr/bin/env python
#

# import system modules
#
import sys
import numpy as np

# function: load
#
# arguments:
#   fname: filename given as command line argument
#
# This method reads a file and returns its contents
#
def load(fname):

    # open matrix files
    #
    with open(fname) as file:
        # split each line of the file into its individual elements
        #
        line = ((file.readline()).rstrip()).split()
        # number of rows equals the first element in the file
        #
        nrows = int(line[0])
        # number of columns equals the second element in the file
        #
        ncols = int(line[1])
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        a = np.zeros((nrows, ncols))
    i = int(0)
    for line in lines:
        j = int(0)
        parts = line.split()
        for part in parts:
            a[i][j] = float(part)
            j += 1
        i += 1
    return a

# function: mmult
#
# arguments:
#   a: operand matrix
#   b: operand matrix
#
# This method multiplies two matrices (a and b) to get an output matrix (c)
#
def mmult(a, b):

    # check dimensions of matrices
    #
    if len(a[0]) != len(b):
        print("Error: check dimensions.")
    
    # set the number of rows and columns
    #
    nrows = len(a)
    ncols = len(b[0])

    # zero output array
    #
    c = np.zeros((nrows, ncols))
    
    # loop over rows of matrix a
    #
    for i in range(len(a)):
        
        # loop over columns of matrix b
        #
        for j in range(len(b[0])):
         
            # loop over rows of matrix b
            #
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c

# function: mprint
#
# arguments:
#   matrix: either the operand matrices or the output matrix
#   label: a label for each line that is printed out
#
# This method prints out both the operand matrices and the output matrix
#
def mprint(matrix, label):
    
    # get the number of rows and columns
    #
    nrows, ncols = matrix.shape
    
    # loop over rows of matrix
    #
    for i in range(nrows):

        # print out each row of the matrix with a label
        #
        print("%s row %d:" % (label, i), end = " ")
        
        for j in range(ncols):
            print("%10.4f" % (matrix[i][j]), end = " ")
        print("")

    # print blank line at end
    #
    print("")
        
    # exit gracefully
    #
    return True

# function: main
#
def main(argv):

    a = load(argv[1])
    b = load(argv[2])
    c = mmult(a, b)
    mprint(a, "'matrix a'")
    mprint(b, "'matrix b'")
    mprint(c, "'matrix c'")

# begin gracefully
#
if __name__ == '__main__':
    main(sys.argv[0:])
#
# end of file

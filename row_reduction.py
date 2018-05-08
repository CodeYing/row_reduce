"""
Function that take a m(row)* n(column) matrix and
row reduce to reduced row echelon form
"""
import operator

def row_reduce(matrix):
    row = len (matrix)
    col = len (matrix[0])
    # for each row in matrix, perform row reduction
    for x in range (0,row):
        while (pos_is_zero(matrix, x)):
            matrix= move_to_last(matrix, x)
        matrix = reduce(x, matrix)
    return matrix

def pos_is_zero(matrix, x):
    """
    check if the x row and x column position is 0
    """
    row = matrix[x]
    return (row[x] == 0)


def move_to_last(matrix, x):
    """
    move the selected row x to the last of the matrix
    """
    move_to_last = [matrix[x]]
    del matrix[x]
    matrix = matrix + move_to_last
    return matrix

def scale(row):
    """
    scale a given row so the leading entry is 1
    """
    factor = row[0]
    if factor != 1:
        row = [x / float(factor) for x in row]
    return row

def reduce_to_zero(row1, row2):
    """
    reduces row2 with a leading entry in a column
    to the right of that of row1
    """
    i = 0
    while (row2[i]== 0):
        i += 1
    factor = row2[i];
    row1 = [x * factor for x in row1]
    row2 = map(operator.sub, row2, row1)
    return row2

def reduce(row, matrix):
    """
    given a specified row, row reduce the entry
    below to 0
    """
    reduced_matrix = []
    for y in matrix[row+1:]:
        first_row = scale(matrix[row])
        reduced_matrix = first_row
        reduced_matrix += reduce_to_zero(matrix[row],y)
    return reduced_matrix

print (row_reduce([[0, 3, -6, 6, 4, -5],
                    [3, -9, 12, -9, 6, 15],
                    [3, -7, 8, -5, 8, 9]]))

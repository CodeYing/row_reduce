"""
A matrix class that takes a m(row)* n(column) matrix and has
a function to row reduce the matrix to Reduced Row Echelon Form
Example:
mtx1 = Matrix([[1, 2], [3, 4]])
"""

class Matrix:
    def __init__(self, values):
        self.n = len(values)
        self.m = len(values[0])
        self.values = []
        for row in values:
            if (len(row) != self.m):
                raise Exception('Col mismatch')
        self.values = values

    def row_reduce(self):
        # row reduce a matrix to its RREF
        for pivot_row in range (0,self.m):
            cur_col_index = pivot_row
            for cur_row_index in range (pivot_row, self.m):
                cur_col_index = find_nonzero(cur_row_index, cur_col_index)
                if cur_col_index < self.m:
                    scale(cur_row_index, cur_col_index)
                    make_zero(cur_row_index, cur_col_index)

    def find_nonzero(self, cur_row_index, cur_col_index):
        """
        Given the current row index and current column index,
        select a nonzero entry in the pivot columnas a pivot,
        swap rows to move this entry into the pivot position
        if necessary.
        Returns the pivot column index
        """
        while (cur_col_index < self.n):
            for r in range (cur_row_index, self.m):
                row = self.values[r]
                if (row[cur_col_index] != 0):
                    swap(cur_col_index, r)
                    break
                else cur_col_index += 1
        return cur_col_index


# mtx1.swap(0, 1) will mutate mtx1 to be
# [[3, 4], [1, 2]]
    def swap(self, row1, row2):
        if (row1 < self.n and row2 < self.n):
            if (row1 != row2):
                newrow1 = self.values[row2]
                newrow2 = self.values[row1]
                self.values[row1] = newrow1
                self.values[row2] = newrow2
        else:
            raise Exception('Col mismatch')

# mtx1.scale(0, 1) will mutate mtx1 to be
# [[0.5, 1], [3, 4]]
# Note: If will throw an exception if the element to scale by is 0 or if the row or the col are out of bound
    def scale(self, row, col):
        if (row < self.m and col < self.n and self.values[row][col] != 0):
            rowValues = self.values[row]
            self.values[row] = map(lambda x : x / float(rowValues[col]), rowValues)
        else:
            raise Exception('Cannot scale')

    def make_zero(self, row, col):

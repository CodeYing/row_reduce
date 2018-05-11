"""
A matrix class that takes a m(row)* n(column) matrix and has
a function to row reduce the matrix to Reduced Row Echelon Form
Example:
mtx1 = Matrix([[0, 3, -6, 6, 4, -5],
              [3, -7, 8, -5, 8, 9],
              [3, -9, 12, -9, 6, 15]])
"""
class Matrix:
    def __init__(self, values):
        self.m = len(values)
        self.n = len(values[0])
        self.values = []
        for row in values:
            if (len(row) != self.n):
                raise Exception('Col mismatch')
        self.values = values

    def row_reduce(self):
        """
        row reduce a matrix to its RREF
        Example:
        print (mtx1.row_reduce) = [[3, -9, 12, -9, 6, 15],
                                   [0, 2, -4, 4, 2, -6],
                                   [0, 0, 0, 0, 1, 4]]
        """
        for pivot_row in range (0,self.m):
            cur_col_index = pivot_row
            for cur_row_index in range (pivot_row, self.m):
                cur_col_index = self.find_nonzero(cur_row_index, cur_col_index)
                if cur_col_index < self.n:
                    self.scale(cur_row_index, cur_col_index)
                    self.make_zero(cur_row_index, cur_col_index)
        # Todo: backward phase row reduction

    def find_nonzero(self, cur_row_index, cur_col_index):
        """
        Given the current row index and current column index,
        select a nonzero entry in the pivot columnas a pivot,
        swap rows to move this entry into the pivot position
        if necessary.
        Returns the pivot column index
        Example:
        print (mtx1.find_nonzero(0, 0)) = 0
        print (mtx1.values) = [[3, -7, 8, -5, 8, 9],
                               [0, 3, -6, 6, 4, -5],
                               [3, -9, 12, -9, 6, 15]])
        """
        while (cur_col_index < self.n):
            for r in range (cur_row_index, self.m):
                row = self.values[r]
                if (row[cur_col_index] != 0):
                    self.swap(cur_row_index, r)
                    return cur_col_index
            cur_col_index += 1
        return cur_col_index

    def swap(self, row1, row2):
        """
        mtx1.swap(0, 1) will mutate mtx1 to be
        [[3, -7, 8, -5, 8, 9],
        [0, 3, -6, 6, 4, -5],
        [3, -9, 12, -9, 6, 15]]
        """
        if (row1 < self.m and row2 < self.m):
            if (row1 != row2):
                newrow1 = self.values[row2]
                newrow2 = self.values[row1]
                self.values[row1] = newrow1
                self.values[row2] = newrow2
        else:
            raise Exception('Col mismatch')

    def scale(self, row, col):
        """
        Scale the row identified by the row index by the pivot
        position(row, col)
        Example:
        mtx1.scale(2,0) will mutate mtx1 to be
        [[0, 3, -6, 6, 4, -5],
        [3, -7, 8, -5, 8, 9],
        [1, -3, 4, -3, 2, 5]]
        Throws exception if the element to scale by is 0
        or if the row or the col are out of bound
        """
        if (row < self.m and col < self.n and self.values[row][col] != 0):
            rowValues = self.values[row]
            self.values[row] = map(lambda x : x / float(rowValues[col]), rowValues)
        else:
            raise Exception('Cannot scale')

    def make_zero(self, row, col):
        """
        Given the pivot position(row, col), reduce rows below to zero
        """
        pivot_row = self.values[row]
        r = row + 1

        while (r < self.m):
            cur_row = self.values[r]
            factor = cur_row[col]
            mult_of_pivot_row = map(lambda x : x * float(factor), pivot_row)
            for x in range (col,self.n):
                self.values[r][x] = cur_row[x] - mult_of_pivot_row[x]
            r += 1

mtx1 = Matrix([[0, 3, -6, 6, 4, -5],
              [3, -7, 8, -5, 8, 9],
              [3, -9, 12, -9, 6, 15]])
mtx1.row_reduce()
print(mtx1.values)

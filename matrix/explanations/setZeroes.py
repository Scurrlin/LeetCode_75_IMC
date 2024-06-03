# Set Matrix Zeroes

def setZeroes(matrix: List[List[int]]) -> None:

# This line defines a function named `setZeroes` that takes a 2D list (matrix)
# of integers as input and returns nothing (`None`). The function is intended to
# modify the input matrix in-place.

    rows, cols = len(matrix), len(matrix[0])

# This line initializes two variables, `rows` and `cols`, with the number of
# rows and columns in the matrix, respectively.

    zero_rows, zero_cols = set(), set()

# This line initializes two sets, `zero_rows` and `zero_cols`, which will be
# used to keep track of the rows and columns that contain a zero.

    for i in range(rows):
        for j in range(cols):

# These lines start a nested loop that will iterate over each element in the
# matrix.

            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

# If the current element is zero, the row and column indices are added to the
# `zero_rows` and `zero_cols` sets, respectively.

    for i in range(rows):
        for j in range(cols):

# These lines start another nested loop that will iterate over each element in
# the matrix again.

            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

# If the current row or column index is in the `zero_rows` or `zero_cols` sets,
# respectively, the current element is set to zero. This effectively sets all
# elements in a row or column to zero if that row or column contained a zero in
# the original matrix.
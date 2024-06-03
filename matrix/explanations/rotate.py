# Rotate Image

def rotate(matrix: List[List[int]]) -> None:

# This line defines a function named `rotate` that takes a 2D list (matrix) of
# integers as an argument and doesn't return anything (`None`).

    n = len(matrix)

# This line sets `n` to the length of the matrix, which is the number of rows
# (or columns, since it's a square matrix).

    for i in range(n // 2):

# This line starts a loop that will iterate over half the rows of the matrix.
# The `//` operator performs integer (floor) division.

        for j in range(i, n - i - 1):

# This line starts a nested loop that will iterate over a subset of the columns
# for each row. The subset starts at the current row index `i` and ends at `n -
# i - 1`.

            temp = matrix[i][j]

# This line saves the current matrix element into a temporary variable `temp`.

            matrix[i][j] = matrix[n - j - 1][i]

# This line replaces the current matrix element with the element from the
# opposite side of the matrix, effectively rotating it 90 degrees clockwise.

            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

# This line continues the rotation by replacing the element we just moved with
# the element from the next side of the matrix.

            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

# This line continues the rotation by replacing the element we just moved with
# the element from the final side of the matrix.

            matrix[j][n - i - 1] = temp

# This line completes the rotation by replacing the final element with the value
# we saved in `temp` at the beginning.

# In summary, this function rotates a square matrix 90 degrees clockwise in
# place (without creating a new matrix). It does this by rotating four elements
# at a time, one from each side of the matrix, using a temporary variable to
# hold one value while the others are being moved.
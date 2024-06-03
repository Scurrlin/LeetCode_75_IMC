# Spiral Matrix

def spiralOrder(matrix: List[List[int]]) -> List[int]:

# This line defines a function named `spiralOrder` that takes a 2D list (matrix)
# of integers as input and returns a list of integers.

    res = []

# This line initializes an empty list `res` that will be used to store the
# elements of the matrix in spiral order.

    while matrix:

# This line starts a while loop that continues as long as the `matrix` is not
# empty.

        res += matrix.pop(0)

# This line removes the first row from the `matrix` and appends its elements to
# the `res` list. The `pop(0)` function removes the first element of the list,
# which in this case is the first row of the matrix.

        matrix = list(zip(*matrix))[::-1]

# This line does three things:
# 1. `*matrix` unpacks the remaining rows of the matrix.
# 2. `zip(*matrix)` transposes the matrix (i.e., rows become columns and vice
#    versa).
# 3. `list(zip(*matrix))[::-1]` converts the zipped object back to a list and
#    reverses it. This effectively rotates the remaining part of the matrix 90
#    degrees counterclockwise.

    return res

# This line returns the list `res`, which now contains the elements of the
# original matrix in spiral order.
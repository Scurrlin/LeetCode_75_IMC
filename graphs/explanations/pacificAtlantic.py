# Pacific Atlantic Water Flow

def pacificAtlantic(matrix: List[List[int]]) -> List[List[int]]:

# This is the function definition for `pacificAtlantic`. It takes a 2D list
# `matrix` as an input and returns a list of lists.

    if not matrix or not matrix[0]:
        return []

# If the matrix is empty or the first row of the matrix is empty, return an
# empty list.

    def dfs(i, j, visited, prevHeight):

# This is a nested function `dfs` within `pacificAtlantic` that takes two
# integers `i` and `j`, a set `visited`, and an integer `prevHeight` as inputs.

        if (i, j) in visited or i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] < prevHeight:
            return

# If the cell `(i, j)` has already been visited, or the cell is out of bounds,
# or the height of the cell is less than `prevHeight`, return without doing
# anything.

        visited.add((i, j))

# Add the cell `(i, j)` to the `visited` set.

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + direction[0], j + direction[1], visited, matrix[i][j])

# For each direction (right, left, down, up), call `dfs` on the cell in that
# direction with the current cell's height as `prevHeight`.

    pacific, atlantic = set(), set()

# Initialize two sets `pacific` and `atlantic`.

    for i in range(len(matrix)):
        dfs(i, 0, pacific, matrix[i][0])
        dfs(i, len(matrix[0]) - 1, atlantic, matrix[i][len(matrix[0]) - 1])

# For each row, call `dfs` on the first cell for `pacific` and the last cell for
# `atlantic`.

    for j in range(len(matrix[0])):
        dfs(0, j, pacific, matrix[0][j])
        dfs(len(matrix) - 1, j, atlantic, matrix[len(matrix) - 1][j])

# For each column, call `dfs` on the first cell for `pacific` and the last cell
# for `atlantic`.

    return list(pacific & atlantic)

# Return the list of cells that can reach both the Pacific and Atlantic oceans.
# This is the intersection of the `pacific` and `atlantic` sets.
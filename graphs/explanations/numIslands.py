# Number of Islands

def numIslands(grid: List[List[str]]) -> int:

# This is the function definition for `numIslands`. It takes a 2D list `grid` as
# an input and returns an integer.

    if not grid:
        return 0

# If the grid is empty, return 0. There are no islands in an empty grid.

    def dfs(i, j):

# This is a nested function `dfs` within `numIslands` that takes two integers
# `i` and `j` as inputs.

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
# If the cell `(i, j)` is out of bounds or the cell is water (`'0'`), return
# without doing anything.

        grid[i][j] = '0'

# Mark the cell `(i, j)` as water. This is to avoid visiting the same cell
# again.

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

# Call `dfs` on the cells to the right, left, down, and up of `(i, j)`.

    count = 0

# Initialize a counter `count` to 0. This will keep track of the number of
# islands.

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

# For each cell in the grid, if the cell is land (`'1'`), call `dfs` on the cell
# and increment `count` by 1.

    return count

# Return the number of islands.
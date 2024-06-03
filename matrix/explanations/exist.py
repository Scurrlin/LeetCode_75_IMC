# Word Search

def exist(board: List[List[str]], word: str) -> bool:

# This line defines a function named `exist` that takes two parameters: `board`
# which is a 2D list of strings, and `word` which is a string. The function
# returns a boolean value.

    def dfs(i, j, k):

# This line defines a nested function named `dfs` that takes three parameters:
# `i`, `j`, and `k`. This function is used for depth-first search on the
# `board`.

        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
            return False

# This line checks if the current position `(i, j)` is within the bounds of the
# `board` and if the character at the current position is equal to the `k`th
# character of `word`. If any of these conditions are not met, it returns
# `False`.

        if k == len(word) - 1:
            return True

# This line checks if we have reached the end of the `word`. If so, it returns
# `True`.

        tmp, board[i][j] = board[i][j], '/'

# This line temporarily stores the current character and marks the current
# position on the `board` as visited by replacing the character with `'/'`.

        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)

# This line performs a depth-first search in all four directions (up, down,
# left, right) from the current position.

        board[i][j] = tmp

# This line restores the character at the current position on the `board`.

        return res

# This line returns the result of the depth-first search.

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True

# These lines iterate over each position on the `board` and start a depth-first
# search from each position. If the `dfs` function returns `True` for any
# position, the `exist` function immediately returns `True`.

    return False

# This line returns `False` if the `dfs` function never returns `True` for any
# position on the `board`. This means that the `word` does not exist on the
# `board`.
# Course Schedule

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:

# This is the function definition for `canFinish`. It takes an integer
# `numCourses` and a list of list of integers `prerequisites` as inputs and
# returns a boolean.

    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

# These lines initialize a list of empty lists `graph` and a list of zeros
# `visited`, both of the same length as `numCourses`.

    for x, y in prerequisites:
        graph[x].append(y)

# This loop populates the `graph` list. For each pair `(x, y)` in
# `prerequisites`, `y` is appended to the list at index `x`.

    def dfs(i):

# This is a nested function `dfs` within `canFinish` that takes an integer `i`
# as an input.

        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True

# If the course `i` is being visited (`visited[i] == -1`), it means there's a
# cycle, so return `False`. If the course `i` has been visited (`visited[i] ==
# 1`), it means no cycle from course `i`, so return `True`.

        visited[i] = -1

# Mark the course `i` as being visited.

        for j in graph[i]:
            if not dfs(j):
                return False

# For each course `j` in the prerequisites of course `i`, if there's a cycle
# from course `j`, return `False`.

        visited[i] = 1
        return True

# After visiting all the prerequisites of course `i`, mark course `i` as
# visited, and return `True`.

    for i in range(numCourses):
        if not dfs(i):
            return False

# For each course `i`, if there's a cycle from course `i`, return `False`.

    return True

# If there's no cycle from any course, return `True`. This means it is possible
# to finish all courses.
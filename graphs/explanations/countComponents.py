# Number of Connected Components in an Undirected Graph (Leetcode Premium)

def countComponents(n: int, edges: List[List[int]]) -> int:

# This is the function definition for `countComponents`. It takes an integer `n`
# and a list of lists `edges` as inputs and returns an integer.

    graph = {i: [] for i in range(n)}

# This line initializes `graph` as a dictionary where each key is a node and the
# value is a list of its neighbors.

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

# These lines populate the `graph` dictionary. For each edge `(a, b)`, `b` is
# added to the list of `a`'s neighbors and `a` is added to the list of `b`'s
# neighbors.

    visited = set()

# This line initializes `visited` as a set to keep track of the nodes that have
# been visited.

    def dfs(node):

# This is a nested function `dfs` within `countComponents` that takes an integer
# `node` as an input.

        if node in visited:
            return

# If `node` has already been visited, return without doing anything.

        visited.add(node)

# This line adds `node` to the `visited` set.

        for neighbor in graph[node]:
            dfs(neighbor)

# This line starts a loop that iterates over each neighbor of `node` and calls
# `dfs` on the neighbor. This is a depth-first search.

    count = 0

# This line initializes `count` to 0. `count` will keep track of the number of
# connected components.

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

# This loop iterates over each node. If a node has not been visited, call `dfs`
# on the node and increment `count` by 1. This counts the number of connected
# components.

    return count

# This line returns `count`, which is the number of connected components in the
# graph.
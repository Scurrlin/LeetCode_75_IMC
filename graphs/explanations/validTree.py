# Graph Valid Tree (Leetcode Premium)

def validTree(n: int, edges: List[List[int]]) -> bool:

# This is the function definition for `validTree`. It takes an integer `n` and a
# list of lists `edges` as inputs and returns a boolean.

    if len(edges) != n - 1:
        return False

# If the number of edges is not equal to `n - 1`, return `False`. A tree with
# `n` nodes must have exactly `n - 1` edges.

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

    def dfs(node, parent):

# This is a nested function `dfs` within `validTree` that takes two integers
# `node` and `parent` as inputs.

        visited.add(node)

# This line adds `node` to the `visited` set.

        for neighbor in graph[node]:

# This line starts a loop that iterates over each neighbor of `node`.

            if neighbor == parent:
                continue

# If `neighbor` is the same as `parent`, skip the current iteration of the loop.

            if neighbor in visited:
                return False

# If `neighbor` has already been visited, return `False`. This means that the
# graph has a cycle.

            if not dfs(neighbor, node):
                return False

# If the recursive call to `dfs` with `neighbor` as `node` and `node` as
# `parent` returns `False`, return `False`.

        return True

# If the function has not returned `False` by this point, return `True`. This
# means that no cycle has been found.

    return dfs(0, -1) and len(visited) == n

# Return `True` if the call to `dfs` with `0` as `node` and `-1` as `parent`
# returns `True` and all nodes have been visited, otherwise return `False`. This
# checks if the graph is a valid tree.
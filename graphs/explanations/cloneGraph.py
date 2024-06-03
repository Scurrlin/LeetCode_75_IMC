# Clone Graph

def cloneGraph(node: 'Node') -> 'Node':

# This is the function definition for `cloneGraph`. It takes a node (which is an
# instance of the class `Node`) as an input and returns a node.

    visited = {}

# This line initializes an empty dictionary `visited`. This will be used to keep
# track of the nodes that have already been cloned.

    def clone(node):

# This is a nested function `clone` within `cloneGraph` that takes a node as an
# input.

        if not node:
            return node

# If the node is `None` (or equivalent), it returns the node. This is the base
# case for the recursion.

        if node in visited:
            return visited[node]

# If the node has already been visited (i.e., cloned), it returns the cloned
# node from the `visited` dictionary.

        clone_node = Node(node.val, [])

# This line creates a new node `clone_node` with the same value as the input
# node but with an empty list of neighbors.

        visited[node] = clone_node

# The cloned node is then added to the `visited` dictionary with the original
# node as the key.

        if node.neighbors:
            clone_node.neighbors = [clone(n) for n in node.neighbors]

# If the original node has neighbors, it clones each neighbor recursively and
# assigns the list of cloned neighbors to `clone_node.neighbors`.

        return clone_node

# The cloned node is returned.

    return clone(node)

# Finally, the `cloneGraph` function calls the `clone` function on the input
# node and returns the result. This starts the process of cloning the graph.
# Binary Tree Level Order Traversal

def levelOrder(root: TreeNode) -> List[List[int]]:

# This line defines a function named `levelOrder` that takes a `TreeNode` as an
# argument and returns a list of lists of integers.

    levels = []

# This line initializes an empty list named `levels` that will hold the values
# of the nodes at each level of the tree.

    if not root:
        return levels

# This block checks if the root of the tree is `None`. If it is, the function
# returns the empty `levels` list.

    def helper(node, level):

# This line defines a nested helper function that takes a node and its level in
# the tree as arguments.

        if len(levels) == level:
            levels.append([])

# This block checks if the current level exists in the `levels` list. If it
# doesn't, it appends an empty list to `levels`.

        levels[level].append(node.val)

# This line appends the value of the current node to its corresponding level in
# the `levels` list.

        if node.left:
            helper(node.left, level + 1)

# This block checks if the current node has a left child. If it does, it
# recursively calls the `helper` function on the left child, incrementing the
# level by 1.

        if node.right:
            helper(node.right, level + 1)

# This block checks if the current node has a right child. If it does, it
# recursively calls the `helper` function on the right child, incrementing the
# level by 1.

    helper(root, 0)

# This line calls the `helper` function on the root of the tree, starting at
# level 0.

    return levels

# This line returns the `levels` list, which now contains the values of the
# nodes at each level of the tree.
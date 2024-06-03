# Maximum Depth of Binary Tree

def maxDepth(root: TreeNode) -> int:

# This line defines a function named `maxDepth` that takes one argument `root`
# of type `TreeNode` and returns an integer. This function is intended to find
# the maximum depth of a binary tree.

    if not root:

# This line checks if the `root` is `None` (i.e., the tree is empty). This is
# the base case for the recursion.

        return 0

# If the `root` is `None`, the function returns `0` because an empty tree has a
# depth of `0`.

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# If the `root` is not `None`, the function calculates the maximum depth of the
# tree. It does this by adding `1` to the maximum of the depths of the left and
# right subtrees. The depths of the left and right subtrees are calculated
# recursively using the `maxDepth` function.
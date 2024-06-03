# Binary Tree Maximum Path Sum

def maxPathSum(root: TreeNode) -> int:

# This line defines a function `maxPathSum` that takes a `root` node of a binary
# tree as input and returns an integer. The `TreeNode` type hint suggests that
# `root` is expected to be an instance of a `TreeNode` class, which is not shown
# in the provided code but is presumably defined elsewhere.

    def max_gain(node):

# This line defines a nested function `max_gain` that takes a node of the binary
# tree as input.

        nonlocal max_sum

# This line declares `max_sum` as nonlocal, which means it refers to a variable
# defined in the nearest enclosing scope that is not global, which is
# `maxPathSum` in this case.

        if not node:
            return 0

# If the node is `None` (which means we've reached a leaf node's child in the
# binary tree), the function returns 0.

        left_gain = max(max_gain(node.left), 0)

# This line recursively calls `max_gain` on the left child of the current node
# and compares the result with 0. It assigns the maximum of these two values to
# `left_gain`.

        right_gain = max(max_gain(node.right), 0)

# This line does the same thing as the previous line, but for the right child of
# the current node.

        price_newpath = node.val + left_gain + right_gain

# This line calculates the sum of the current node's value and the maximum gains
# from the left and right children. This represents the maximum path sum that
# includes the current node and both of its children.

        max_sum = max(max_sum, price_newpath)

# This line updates `max_sum` to be the maximum of the current `max_sum` and
# `price_newpath`.

        return node.val + max(left_gain, right_gain)

# This line returns the maximum path sum that includes the current node and
# either its left child or its right child (but not both).

    max_sum = float('-inf')

# This line initializes `max_sum` to negative infinity before the first call to
# `max_gain`.

    max_gain(root)

# This line starts the recursion by calling `max_gain` on the root of the binary
# tree.

    return max_sum

# Finally, this line returns the maximum path sum found in the binary tree.
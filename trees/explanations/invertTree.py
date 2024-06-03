# Invert/Flip Binary Tree

def invertTree(root: TreeNode) -> TreeNode:

# This line defines a function named `invertTree` that takes a `TreeNode` as an
# argument and returns a `TreeNode`. The `TreeNode` is assumed to be the root of
# a binary tree.

    if not root:

# This line checks if the root node is `None` (which means the tree is empty).
# If it is, the function returns `None`.
        
        return None
# This line returns `None` if the root node is `None`.

    root.left, root.right = invertTree(root.right), invertTree(root.left)

# This line is where the tree inversion happens. It recursively calls
# `invertTree` on the right and left children of the root node, and then swaps
# them. This effectively inverts the tree.

    return root

# This line returns the root of the inverted tree. Since the inversion is done
# in-place (i.e., the original tree is modified), this is the same node that was
# passed in, but its left and right children have been swapped.
# Lowest Common Ancestor of a Binary Search Tree

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

# This line defines a function `lowestCommonAncestor` that takes three
# arguments: `root`, `p`, and `q`, which are instances of `TreeNode`. The
# function is expected to return an instance of `TreeNode`.

    while root:

# This line starts a loop that continues as long as `root` is not `None`. This
# loop is used to traverse the binary search tree (BST).

        if p.val > root.val and q.val > root.val:

# This line checks if the values of both `p` and `q` are greater than the value
# of `root`. If they are, it means both `p` and `q` are in the right subtree of
# `root`.

            root = root.right

# This line updates `root` to its right child if the above condition is met.

        elif p.val < root.val and q.val < root.val:

# This line checks if the values of both `p` and `q` are less than the value of
# `root`. If they are, it means both `p` and `q` are in the left subtree of
# `root`.

            root = root.left

# This line updates `root` to its left child if the above condition is met.

        else:

# This line starts the `else` block. This block is executed if neither of the
# above conditions is met. This means `p` and `q` are in different subtrees of
# `root` or one of them is `root` itself.

            return root

# This line returns `root` if the above condition is met.

# This function essentially finds the lowest common ancestor (LCA) of two nodes
# `p` and `q` in a BST. The LCA is defined between two nodes `p` and `q` as the
# lowest node in the tree that has both `p` and `q` as descendants (where we
# allow a node to be a descendant of itself). The unique properties of a BST
# provide a shortcut to find the LCA: starting from the root, if both `p` and
# `q` are in the right subtree, then the LCA must be in the right subtree; if
# both are in the left subtree, then the LCA must be in the left subtree;
# otherwise, the LCA must be the current node.
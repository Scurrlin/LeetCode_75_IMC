# Same Tree

def isSameTree(p: TreeNode, q: TreeNode) -> bool:

# This line defines a function `isSameTree` that takes two parameters `p` and
# `q`, both of type `TreeNode`. The function returns a boolean value.

    if not p and not q:

# This line checks if both `p` and `q` are `None` (or falsey). This is the base
# case of the recursion, meaning if both trees are empty, they are considered
# the same.

        return True

# If the above condition is true (both `p` and `q` are `None`), the function
# returns `True`, indicating that the two trees are the same.

    if not p or not q or p.val != q.val:

# This line checks if either `p` or `q` is `None`, or if the values of the root
# nodes of `p` and `q` are not equal. This is another base case of the
# recursion, meaning if one tree is empty and the other is not, or if the root
# nodes of the two trees have different values, the trees are not the same.

        return False

# If the above condition is true (either `p` or `q` is `None`, or `p.val` is not
# equal to `q.val`), the function returns `False`, indicating that the two trees
# are not the same.

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# If none of the above conditions are true, the function recursively calls
# itself on the left and right children of `p` and `q`. The function will return
# `True` only if both the left and right subtrees are the same. This is the
# recursive case of the function, allowing it to traverse the entire tree.
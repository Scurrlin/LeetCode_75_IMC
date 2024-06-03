# Subtree of Another Tree

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:

# This line defines a function `isSubtree` that takes two arguments: `root` and
# `subRoot`, both of which are expected to be instances of `TreeNode`. The
# function is expected to return a boolean value.

    if not subRoot:

# This line checks if `subRoot` is `None` or not. If `subRoot` is `None`, it
# means there is no subtree to check, so the function should return `True`.

        return True
    
# This line returns `True` if the previous condition (`if not subRoot`) is met.

    if not root:

# This line checks if `root` is `None` or not. If `root` is `None`, it means
# there is no tree to check against, so the function should return `False`.

        return False

# This line returns `False` if the previous condition (`if not root`) is met.

    if isSameTree(root, subRoot):

# This line checks if the tree rooted at `root` is the same as the tree rooted
# at `subRoot` by calling the function `isSameTree`. If they are the same, then
# `subRoot` is a subtree of `root`.

        return True

# This line returns `True` if the previous condition (`if isSameTree(root,
# subRoot)`) is met.

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# If none of the above conditions are met, the function calls itself recursively
# for the left and right children of the `root`. If `subRoot` is a subtree of
# either the left or the right subtree of `root`, the function will return
# `True`. Otherwise, it will return `False`.
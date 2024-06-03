# Serialize and Deserialize Binary Tree

class Codec:

# This line defines a new class named `Codec`.

    def serialize(self, root):

# This line defines a method named `serialize` within the `Codec` class. This
# method takes a binary tree and converts it into a string.

        def rserialize(root, string):

# This line defines a helper function `rserialize` within the `serialize`
# method. This function is recursive and is used to traverse the binary tree.

            if root is None:
                string += "None,"

# If the current node is `None` (i.e., the tree is empty or it's a leaf node),
# append the string "None," to the string.

            else:
                string += str(root.val) + ","

# If the current node is not `None`, append the value of the node and a comma to
# the string.

                string = rserialize(root.left, string)
                string = rserialize(root.right, string)

# Recursively call `rserialize` on the left and right children of the current
# node.

            return string

# Return the string after traversing the entire tree.

        return rserialize(root, "")

# Call the `rserialize` function on the root of the tree with an empty string as
# the initial string.

    def deserialize(self, data):

# This line defines a method named `deserialize` within the `Codec` class. This
# method takes a string and converts it back into a binary tree.

        def rdeserialize(l):

# This line defines a helper function `rdeserialize` within the `deserialize`
# method. This function is recursive and is used to rebuild the binary tree from
# the string.

            if l[0] == "None":
                l.pop(0)
                return None

# If the first element in the list is "None", remove it from the list and return
# `None`.

            root = TreeNode(l[0])
            l.pop(0)

# Create a new tree node with the first element in the list as its value, and
# remove that element from the list.

            root.left = rdeserialize(l)
            root.right = rdeserialize(l)

# Recursively call `rdeserialize` to construct the left and right subtrees.

            return root
# Return the root of the constructed tree.

        data_list = data.split(',')

# Split the input string into a list of strings using the comma as a delimiter.

        root = rdeserialize(data_list)

# Call the `rdeserialize` function on the list to construct the binary tree.

        return root

# Return the root of the constructed tree.
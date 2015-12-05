"""
    Here's the assignment:
        Find the max height of a tree T.
        You're given a pointer `T` to the root node of the tree.
        You can also assume a Node class, where every Node object has:
            `left` attribute pointing to node's left child
            `right` attribute pointing to node's right child

    Constraints:
        None

    Implementation considerations:
        None
"""

def tree_height(T):
    if T.left == None and T.right == None:
        return 1
    else:
        left_subtree_height = 1 + tree_height(T.root.left)
        right_subtree_height = 1 + tree_height(T.root.right)
        max_height = left_subtree_height if left_subtree_height > right_subtree_height else right_subtree_height
        return max_height
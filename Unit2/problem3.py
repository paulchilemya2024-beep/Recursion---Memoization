# LeetCode 226 — Invert Binary Tree
# Given a binary tree, swap every left and right child in the entire tree.
#     4                 4
#    / \               / \
#   2   7     →       7   2
#  / \ / \           / \ / \
# 1  3 6  9         9  6 3  1


class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
         self.value = value
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if not root:
            return None
        #Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# Build example tree
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

# Invert it
new_root = Solution().invertTree(root)
print(new_root)

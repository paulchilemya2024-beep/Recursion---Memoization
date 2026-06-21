# LeetCode 617 — Merge Two Binary Trees 
# You’re given two binary trees, and you must merge them into one tree.
# Rules:
# If both nodes exist, the new node’s value = t1.val + t2.val
# If only one node exists, use that node. If both are null, return null


class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
         self.value = value
         self.left = left
         self.right = right

    

class Solution:
     def mergeTrees(self, t1:TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or t2:
            return t1, t2
        
        v1 = t1.value if t1 else 0
        v2 = t2.value if t2 else 0

        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return root
# Tree 1
t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

# Tree 2
t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)

merged = Solution().mergeTrees(t1, t2)
print(merged)

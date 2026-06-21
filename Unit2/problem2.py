
#  LeetCode 1448 — Count Good Nodes in Binary Tree 
# A node is good if On the path from the root to that node,
# no value is greater than the node’s value. In other words:The node is ≥ every
# value on the path above it.

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
         self.value = value
         self.left = left
         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.value >= maxVal else 0

            maxVal = max(maxVal, node.value)

            res +=dfs(node.left, maxVal)
            res += dfs(node.right,maxVal)
            return res
        return dfs(root, root.value)

# Time: O(n) — visit each node once

# Space: O(h) — recursion stack (h = tree height)

root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)

print(Solution().goodNodes(root1))  # Expected: 4

        
                       
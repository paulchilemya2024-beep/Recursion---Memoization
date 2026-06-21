# LeetCode 110 is Balanced Binary Tree. You check whether every node’s 
# left and right subtrees differ in height by no more than 1,
# and both subtrees are themselves balanced.

class TreeNode:
    def __init__(self, value=0, left = None, right =None):
        self.value = value
        self.left = left
        self.right = right

    

class Solution:
    def isBalanced(self, root):
        def height(node):
            #base case: Empty tree has height of 0
            if not node:
                return 0
            #Get height of left subtree
            left = height(node.left)
            if left ==-1:
                #if left tree is unblanced, propogate upwards
                return -1
            #get height of right subtree
            right = height(node.right)
            if right ==-1:
                return -1
            
            #if current nodes subtrees differ by more than 1, this is unbalanced

            if abs(left - right) > 1:
                return -1
            
            #return the actual height of this subtree 
            return 1 + max(left, right)
        return height(root) != -1
    
# Balanced tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

solution = Solution().isBalanced(root1)
print(solution)


# Time: 𝑂(𝑛)

# Space: 𝑂(ℎ)where ℎ is tree height (worst case 𝑂(𝑛), best case 𝑂(log𝑛))
            

        
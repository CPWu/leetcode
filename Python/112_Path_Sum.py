# 4 Possible Solutions
# 1. Recursion
# 2. Iteration

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    # Time: O(N), Space: O(N)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currentSum):
            if not node:
                return False
            
            currentSum += node.val
            if not node.left and not node.right:
                return currentSum == targetSum
        
            return (dfs(node.left, currentSum) or dfs(node.right, currentSum))
        
        return dfs(root, 0)

    # Iterative
    # Time: O(N), Space:(N)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        currentSum = 0
        
        stack = [(root,currentSum + root.val)]
        
        while stack:
            node, currentSum = stack.pop()
            if not node.left and not node.right and targetSum == currentSum:
                return True
            if node.left:
                stack.append((node.left, currentSum + node.left.val))
            if node.right:
                stack.append((node.right, currentSum + node.right.val))
            
        return False
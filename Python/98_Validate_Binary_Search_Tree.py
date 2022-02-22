# 1 Possible Solutions
# Recursive
# Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive 
    # Time: O(N), Space: O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Nested Function
        def valid(node, left, right):
            # If BST is empty it is still a valid BST
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False

            # Left subtree has to be less than the parent node.val)
            # Right subtree has to be greater than the parent node.val)
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))             

        return valid(root, float("-inf"), float("inf"))

    # Iterative
    # Time: O(N), Space: O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # If BST is empty it is still a valid BST
        if not root: 
            return True
        
        # Use Stack to Run through nodes
        stack = [(root, float("-inf"), float("inf"))]
        
        while stack:
            root, lowerBound, upperBound = stack.pop()
            if not root:
                continue
            value = root.val
            if value <= lowerBound or value >= upperBound:
                return False
            stack.append((root.right, value, upperBound))
            stack.append((root.left, lowerBound, value))
        return True
            
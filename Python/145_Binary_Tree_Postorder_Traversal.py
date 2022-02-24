# 4 Possible Solutions
# 1. Iterative - One Stack
# 2. Iterative
# 3. Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Two Stack
    # Time: O(N), Space: O(H)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty Tree
        if not root:
            return None
        
        stack = [root]
        result = []
        
        while stack:
            currentNode = stack.pop()
            result.append(currentNode.val)
            
            if currentNode.left:
                stack.append(currentNode.left)
                
            if currentNode.right:
                stack.append(currentNode.right)
                
        
        return result[::-1]

    # Recursion
    # Time: O(N), Space: O(H)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty Tree
        if not root:
            return None
        
        result = []
        
        def _postOrderTraversal(node, result):
            if node:
                _postOrderTraversal(node.left, result)
                _postOrderTraversal(node.right, result)
                result.append(node.val)
                
        _postOrderTraversal(root, result)
        
        return result
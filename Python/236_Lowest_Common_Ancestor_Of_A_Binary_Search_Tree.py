# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time: O(log N), Space O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Cases:
        # 1. One node in Left/Right Tree
        # 2. Both nodes are in left tree
        # 3. Both nodes are in right tree
        # 4. One node is ancestor and other node is in left or right tree
        
        currentNode = root
        
        while currentNode:
            # Case #3 
            if p.val > currentNode.val and q.val > currentNode.val:
                currentNode = currentNode.right
            # Case #2
            elif p.val < currentNode.val and q.val < currentNode.val:
                currentNode = currentNode.left
            else:
                return currentNode
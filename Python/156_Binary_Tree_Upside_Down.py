# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(log N)/N, Space: O(H)
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(current):
            if not current.left:
                return current
            
            newRoot = dfs(current.left)
            current.left.left = current.right
            current.left.right = current
            current.left = None
            current.right = None
            
            return newRoot
        
        if not root:
            return None
        
        return dfs(root)
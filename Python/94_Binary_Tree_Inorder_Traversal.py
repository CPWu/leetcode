# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#         self._preorderTraversal(root, result)
#         return result

#     ## Recursive
#     def _preorderTraversal(self, root, result):
#         if root:
#             result.append(root.val)
#             self._preorderTraversal(root.left, result)
#             self._preorderTraversal(root.right, result)

    ## Iterative
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result, stack = [], [root]
        
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result


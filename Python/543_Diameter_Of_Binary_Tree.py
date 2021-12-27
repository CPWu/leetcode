# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # We use a list so diameter is pass by reference
        diameter = []
        diameter.append(0)

        self.dfs(root, diameter)

        return diameter[0]


    def dfs(node, diameter):
        if node.left is None and node.right is None:
            return 0
        
        left_height, right_height = 0, 0

        if node.left is not None:
            left_height = 1 + self.dfs(node.left, diameter)
        if node.right is not None:
            right_height = 1 + self.dfs(node.right, diameter)
        
        if left_height + right_height > diameter[0]:
            diameter[0] = left_height + right_height

        return max(left_height, right_height)
# 2 Possible Solutions
# 1. Recursion
# 2. Iteration


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Recursion
    # Time: O(H) - AVG(log N)/Worst(N), Space: O(H)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        def insert(node, value):
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
        
        insert(root, val)

        return root

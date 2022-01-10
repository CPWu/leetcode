# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Time: O(N), Space: O(N)
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.result = None

        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            currentNode = (node == p) or (node == q)
            if (left and right) or (currentNode and right) or (currentNode and left):
                self.result = node
                return

            return left or right or currentNode
        
        dfs(root)
        return self.result
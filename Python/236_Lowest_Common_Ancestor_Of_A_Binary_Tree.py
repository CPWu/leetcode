# Definition for a binary tree node.
# class TreeNode:
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

        # Cases:
        # 1. One node in Left/Right Tree
        # 2. Both nodes are in left tree
        # 3. Both nodes are in right tree
        # 4. One node is ancestor and other node is in left or right tree
        def dfs(currentNode):
            if not currentNode:
                return None
            

            if currentNode == p or currentNode == q:
                return currentNode

            # Go down the left tree
            left = dfs(currentNode.left)
            # Go down the right tree
            right = dfs(currentNode.right)

            # Case #1
            if left and right:
                return currentNode

            # Second Case
            return left if left else right
        
        return dfs(root)

    # Time: O(N), Space: O(N)
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Cases:
        # 1. One node in Left/Right Tree
        # 2. Both nodes are in left tree
        # 3. Both nodes are in right tree
        # 4. One node is ancestor and other node is in left or right tree

        self.result = None
        
        def dfs(currentNode):
            if not currentNode:
                return False
            
            left = dfs(currentNode.left)
            right = dfs(currentNode.right)
            
            current = (currentNode == p) or (currentNode == q)
            
            if (left and right) or (left and current) or (right and current):
                self.result = currentNode
                return
        
            return left or right or current
        
        dfs(root)
        return self.result
          
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Time: O(N), Space: O(N)
    # Iterative/Brute Force
    # def rangeSumBST(self, root, low, high):
    #     """
    #     :type root: TreeNode
    #     :type low: int
    #     :type high: int
    #     :rtype: int
    #     """

    #     if not root:
    #         return 0
    #     answer = 0

    #     if root.val >= low and root.val <= high:
    #         answer += root.val
        
    #     answer += self.rangeSumBST(root.left, low, high)
    #     answer += self.rangeSumBST(root.right, low, high)

    #     return answer

    # Time: O(), Space: O(N)
    # Interative
    # DFS
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        stack = [root]
        answer = 0
        while stack:
            currentNode = stack.pop()
            if currentNode:
                if currentNode.val >= low and currentNode.val <= high:
                    answer += currentNode.val
                if currentNode.val > low:
                    stack.append(currentNode.left)
                if currentNode.val < high:
                    stack.append(currentNode.right)

        return answer

    # # Time: O(N), Space: O(N)
    # # Recursursion
    # def rangeSumBST(self, root, low, high):
    #     self.answer = 0
    #     def dfs(currentNode):
    #         if currentNode:
    #             return 
    #         if low <= currentNode.val <= high:
    #             self.answer += currentNode.val
    #         if low <= currentNode.val:
    #             dfs(currentNode.left)
    #         if currentNode.val <= high:
    #             dfs(currentNode.high)
        
    #     dfs(root)
    #     return self.answer

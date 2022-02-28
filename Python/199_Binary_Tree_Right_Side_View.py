# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root is None:
#             return []

#         right_side = []

#         def dfs(node, level):
#             if level == len(right_side):
#                 right_side.append(node.val)
#             for child in (node.right, node.left):
#                 if child:
#                     dfs(child, level + 1)

#         dfs(root, 0)
#         return right_side

    # BFS
    # Time: O(N), Space: (N)
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
            
        visibleValues = []
        
        queue = deque([root])
        
        while queue:
            levelLength = len(queue)
            for i in range(levelLength):
                currentNode = queue.popleft()
                if i == levelLength - 1:
                    visibleValues.append(currentNode.value)
                    
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
        return visibleValues
                
                    
        
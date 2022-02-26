# 2 Possible Solutions
# 1. Iterative
# 2. Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
# Recursive
# Time: O(N), Space:(H)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handles an empty tree
        if not root:
            return 
        
        queue = deque([root])
        result = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                # Pop nodes in that level and add to result
                currentNode = queue.popleft()
                level.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.append(level)
            
        return result

    # Iterative
    # Time: O(N), Space:(H)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root])
        
        while queue:
            # Start the current level
            levels.append([])
            
            # number of elements in this level
            level_length = len(queue)
            
            for node in range(len(queue)):
                currentNode = queue.popleft()
                # Fulfill the current level
                levels[level].append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            level += 1
        return levels
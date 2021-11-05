"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        result, queue = [], deque()
        queue.append(root)
        
        while len(queue) > 0:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                current_node = queue.popleft()
                level.append(current_node.val)
                for child in current_node.children:
                    queue.append(child)
            result.append(level)
        return result
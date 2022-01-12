"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# Time: O(h), Space: O(1)
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        if p is None or q is None:
            return 
        
        if p == q:
            return p
        
        pointerP = p
        pointerQ = q
        
        while (pointerP != pointerQ):
            pointerP = pointerP.parent if pointerP.parent else q
            pointerQ = pointerQ.parent if pointerQ.parent else p
        
        
        return pointerQ
            
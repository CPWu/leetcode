# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    # DFS
    # Time: O(N), Space: O(N)
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        def dfs(nestedList, depth):
            total = 0
            for item in nestedList:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total
        
        return dfs(nestedList, 1)
    
#     # BFS
#     # Time: O(N), Space: O(N)
#     def depthSum(self, nestedList):
#         """
#         :type nestedList: List[NestedInteger]
#         :rtype: int
#         """
        
#         queue = deque(nestedList)

#         depth = 1
#         total = 0

#         while len(queue) > 0:
#             for i in range(len(queue)):
#                 nested = queue.pop()
#                 if nested.isInteger():
#                     total += nested.getInteger() * depth
#                 else:
#                     queue.extendleft(nested.getList())
#             depth += 1

#         return total
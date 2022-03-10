# 2 Possible Solutions
# 1. BFS with Sort
# 2. BFS with no sort.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(NlogN), Space: O(N)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return none
        
        # Dictionary used to keep track of column
        # Order the nodes within the dictionary list so we are aware of tree level
        columnTable = defaultdict(list)
        
        queue = deque([(root, 0)])
        
        # While queue not empty, traverse:
        while queue:
            node, column = queue.popleft()
            
            if node:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                
        return [columnTable[x] for x in sorted(columnTable.keys())]
    
    # Time: O(N), Space: O(N)
    # Keep track of min, max column so that we do not need to sort and achieve O(N) rather than NLogN
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        columnTable = defaultdict(list)
        min_column, max_column = 0,0
        queue = deque([(root, 0)])
        
        while queue:
            node, column = queue.popleft()
            
            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                
        return [columnTable[x] for x in range(min_column, max_column + 1)]
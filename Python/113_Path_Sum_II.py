# 1 Possible Solutions
# 1. Recursive
# 2. Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive
    # Time: O(N), Space: O(N)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # Empty
        if not root:
            return []
        # Return List
        result = []
        
        def dfs(node, currentPath, currentSum):
            currentSum += node.val
            tempPath = currentPath + [node.val]
            if node.left:
                dfs(node.left, tempPath, currentSum)
            if node.right:
                dfs(node.right, tempPath, currentSum)         
            if not node.left and not node.right and currentSum == targetSum:
                result.append(tempPath)
            
        dfs(root, [], 0)
            
        return result
            
    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]
    
    # BFS + queue    
    def pathSum3(self, root, sum): 
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
        
    # DFS + stack I  
    def pathSum4(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 
    
    # DFS + stack II   
    def pathSum5(self, root, s): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res


        rst.append(path[:])
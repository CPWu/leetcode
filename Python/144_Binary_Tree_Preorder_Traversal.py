# 2 Possible Solutions
# 1. Iterative
# 2. Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # Iterative
# # Time: O(N), Space:(H)
# def preorder(root):
#     # Empty Tree
#     if not root:
#         return []
#     stack = [root]
#     result = []
    
#     while stack:
#         currentNode = stack.pop()
#         if currentNode:
#             result.append(currentNode.value)
#             stack.append(currentNode.right)
#             stack.append(currentNode.left)
        
#     return result

# Recursive
# Time: O(N), Space:(H)
def preorder(root):
    if not root:
        return []
    result = []
    
    def _preorderTraversal(root, result):
        if root:
            result.append(root.value)
            _preorderTraversal(root.left, result)        
            _preorderTraversal(root.right, result)

    _preorderTraversal(root, result)
    
    return result
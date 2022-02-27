# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        stack = []
        
        for val in preorder:
            node = TreeNode(val)
            if not root:
                root = node
            elif val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < val:
                    previousNode = stack.pop()
                previousNode.right = node
            stack.append(node)
            
        return root
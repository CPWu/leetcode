# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(N), Space: O(N)
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # First we need to have a list with the node / node.vals in acscending order, which is in-order traversal
        
        def inorder_traversal(root):
            # If root does not exist
            if not root:
                return []
                
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
     
        nums = inorder_traversal(root)
        
        def constructBST(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            middle = len(nums) // 2
            new_node = TreeNode(nums[middle])
            new_node.left = constructBST(nums[:middle])
            new_node.right = constructBST(nums[middle+1:])
            return new_node
        
        return constructBST(nums)
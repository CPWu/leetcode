# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sortedList = []
        
        while head:
            sortedList.append(head.val)
            head = head.next

        return self.sortedListToBSTHelper(sortedList, 0, len(sortedList)-1)

    def sortedListToBSTHelper(self,sortedList, startIndex, endIndex):
        if startIndex > endIndex:
            return None
        
        middle = (startIndex + endIndex) // 2
        root = TreeNode(sortedList[middle])
        if endIndex == startIndex:
            return root
        else:
            root.left = self.sortedListToBSTHelper(sortedList, startIndex, middle-1)
            root.right = self.sortedListToBSTHelper(sortedList, middle+1, endIndex)
        return root



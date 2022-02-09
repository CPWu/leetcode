# 2 Possible Solutions
# 1. Recursion
# 2. Iterative

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursion
    # Time: O(n + m), Space: O(n + m)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if both lists are empty:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


    # Iterative
    # Time: O(n+m), Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        preHead = ListNode()
        previousNode = preHead
        
        while list1 and list2:
            if list1.val <= list2.val:
                previousNode.next = list1
                list1 = list1.next
            else:
                previousNode.next = list2
                list2 = list2.next
            previousNode = previousNode.next
        
        if list1:
            previousNode.next = list1
        elif list2:
            previousNode.next = list2
        
        return preHead.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: find prevA (node just before index a)
        prevA = list1
        for _ in range(a - 1):
            prevA = prevA.next
        
        # Step 2: find afterB (node just after index b)
        afterB = prevA
        for _ in range(b - a + 2):
            afterB = afterB.next
        
        # Step 3: connect prevA to list2
        prevA.next = list2
        
        # Step 4: find tail of list2
        tail = list2
        while tail.next:
            tail = tail.next
        
        # Step 5: connect tail to afterB
        tail.next = afterB
        
        return list1

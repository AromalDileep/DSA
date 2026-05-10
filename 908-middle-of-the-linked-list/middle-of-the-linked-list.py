# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 0 
        l_index = {}

        curr = head 

        while curr:
            l_index[index] = curr
            index += 1
            curr= curr.next 
        mid = index // 2 

        return l_index[mid]

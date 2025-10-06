# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return None 
        
        last_element = head 
        length = 1 

        while last_element.next:
            last_element = last_element.next
            length += 1 
        
        k = k % length

        last_element.next = head 

        tempNode = head 

        for _ in range(length - k - 1):
            tempNode = tempNode.next

        answer = tempNode.next
        tempNode.next = None 

        return answer

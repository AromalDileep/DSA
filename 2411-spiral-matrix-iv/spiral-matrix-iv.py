# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        mat = [[-1] * n for _ in range(m)]

        top = 0
        bottom = m - 1
        left = 0 
        right = n - 1 

        curr = head

        while curr and top <= bottom and left <= right:

            # left -> right
            for i in range(top, right+1):
                if not curr:
                    return mat
                mat[top][i] = curr.val
                curr = curr.next
            top += 1

            # right -> bottom
            for j in range(top ,bottom+1):
                if not curr:
                    return mat
                mat[j][right] = curr.val
                curr = curr.next
            right -= 1 
            
            # right -> left
            if top <= bottom:
                for i in range(right ,left-1, -1):
                    if not curr:
                        return mat
                    mat[bottom][i] = curr.val
                    curr = curr.next
                bottom -=1
            
            # bottom -> top
            if left <= right:
                for j in range(bottom, top-1, -1):
                    if not curr:
                        return mat
                    mat[j][left] = curr.val
                    curr = curr.next
                left += 1
        return mat   

                
            
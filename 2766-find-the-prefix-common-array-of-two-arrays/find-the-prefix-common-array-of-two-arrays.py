class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        a_set = set()
        b_set = set()
        
        n = len(A)
        res = []
        for i in range(n):
            a_set.add(A[i])
            b_set.add(B[i])
            temp = len(list((a_set) & (b_set)))
            res.append(temp)
        
        return res
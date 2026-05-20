class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)
        freq = defaultdict(int)

        common = 0
        res = []

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
            
            freq[B[i]] += 1 
            if freq[B[i]] == 2:
                common += 1 
            
            res.append(common)
        
        return res
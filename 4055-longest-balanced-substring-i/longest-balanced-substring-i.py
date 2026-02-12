class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1 
                equal = all(v1 == v2 for v1 in freq.values() for v2 in freq.values())
                if equal:
                    ans = max(ans, j-i+1)

        
        return ans

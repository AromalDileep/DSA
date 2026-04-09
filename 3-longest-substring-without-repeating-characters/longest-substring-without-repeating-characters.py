class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        seen = set()
        length = 0 
        l = 0
        
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            length = max(length, r-l+1)
        
        return length

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_count = Counter(s1)

        s2_count = Counter(s2[:n])
        l = 0

        for r in range(n, len(s2)):
            if s1_count == s2_count:
                return True
            
            s2_count[s2[r]] += 1
            s2_count[s2[l]] -= 1
            l += 1
        
        return s1_count == s2_count
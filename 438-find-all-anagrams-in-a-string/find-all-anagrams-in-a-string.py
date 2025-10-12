class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = ''.join(sorted(p))
        l, r = 0, len(p)-1
        res = []
        while r < len(s):
            if ''.join(sorted(s[l:r+1])) == p: 
                res.append(l)
            l += 1 
            r += 1
        return res
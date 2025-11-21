class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        res = set() #(mid_c, outer_c)
        
        left = set()
        right = Counter(s)


        for mid in s: 
            right[mid] -= 1
            
            for char in left:
                if right[char] > 0:
                    res.add((mid, char))
            left.add(mid)


        return len(res)
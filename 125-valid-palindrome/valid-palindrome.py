class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        
        i, j = 0, len(res)-1

        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        
        return True
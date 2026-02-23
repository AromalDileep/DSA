class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = "" 
        for i in range(len(s)):
            l = i
            r = len(s) - 1
            while l <= r:  
                temp = s[l:r + 1]  
                if temp == temp[::-1]:  
                   
                    if len(temp) > len(longest_pal):
                        longest_pal = temp
                r -= 1
        return longest_pal 
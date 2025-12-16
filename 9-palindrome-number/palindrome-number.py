
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if len(str_x)==1:
            return True
        
        return str_x == str_x[::-1]

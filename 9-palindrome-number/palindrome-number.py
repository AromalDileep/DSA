
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if len(str_x)==1:
            return True
        for i in range(int(len(str_x)/2)):
            if str_x[i] != str_x[len(str_x) - 1 - i]:
                return False
        return True

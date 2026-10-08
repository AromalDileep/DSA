class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        n = len(s)
        i = 0
        open_count = 0
        close_count = 0
        index = 0 
        result = ""

        while i < n:
            if s[i] == "(":
                open_count += 1
            else:
                close_count += 1 
            if open_count == close_count:
                result += s[index+1: i]
                index = i+1         

            i += 1

        return result
        

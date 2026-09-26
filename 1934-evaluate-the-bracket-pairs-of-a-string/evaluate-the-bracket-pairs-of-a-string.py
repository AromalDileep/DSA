class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        pairs = {}
        for key, val in knowledge:
            pairs[key] = val
        
        l = 0
        result = ""
        while l < len(s):
            if s[l] == "(":
                r = l+1
                while s[r] != ")":
                    r += 1
                result += pairs.get(s[l+1:r], "?")
                l = r+1 
            else:
                result += s[l]
                l += 1
        
        return result
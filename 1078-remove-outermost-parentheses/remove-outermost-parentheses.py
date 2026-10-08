class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        result = []
        opened = 0

        for para in s:
            if para == "(":
                if opened > 0:
                    result.append(para)
                opened += 1
            
            else:
                opened -= 1

                if opened >0:
                    result.append(para)
        
        return "".join(result)

                


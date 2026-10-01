class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for para in s:
            if para in close_to_open:
                if len(stack) == 0:
                    return False
                if stack.pop() != close_to_open.get(para, 0):
                    return False
            
            else:
                stack.append(para)
        
        return len(stack) == 0
                
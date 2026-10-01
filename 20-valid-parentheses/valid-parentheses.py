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
                if not stack or stack.pop() != close_to_open[para]:
                    return False
            
            else:
                stack.append(para)
        
        return len(stack) == 0
                
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
        
            if p == "]":
                if not stack:
                    if not stack:
                        return False
                temp = stack.pop()
                if temp != "[":
                    return False
            elif p == ")":
                if not stack:
                    return False
                temp = stack.pop()
                if temp != "(":
                    return False
            elif p == "}":
                if not stack:
                    return False
                temp = stack.pop()
                if temp != "{":
                    return False

        
        return len(stack) == 0
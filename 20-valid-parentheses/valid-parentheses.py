class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for br in s:
            if br not in close_to_open:
                stack.append(br)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if temp != close_to_open[br]:
                    return False
        
        return len(stack) == 0
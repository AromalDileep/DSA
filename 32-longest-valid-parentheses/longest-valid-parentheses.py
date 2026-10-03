class Solution:
    def longestValidParentheses(self, s: str) -> int:

        longest = 0
        stack = [-1]

        for i, para in enumerate(s):
            if para == "(":
                stack.append(i)

            
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i -stack[-1])
        
        return longest
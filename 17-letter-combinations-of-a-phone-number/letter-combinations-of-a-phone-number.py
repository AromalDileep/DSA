from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_num = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def backtrack(index, path):
            # Base case: if the path is complete
            if index == len(digits):
                res.append("".join(path))
                return
            
            # Get letters corresponding to the current digit
            for ch in phone_num[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()  # backtrack step

        backtrack(0, [])
        return res

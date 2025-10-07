class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(start):
            #  base case
            if len(sol) == k:
                res.append(sol.copy())
                return

            #  loop through remaining numbers
            for i in range(start, n + 1):
                sol.append(i)
                backtrack(i + 1)   # move to the next number
                sol.pop()          # backtrack

        backtrack(1)
        return res

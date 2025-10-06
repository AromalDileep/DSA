class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # Base case
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            # Explore choices
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # allow reuse (i)
                path.pop()

        backtrack(0, [], 0)
        return res

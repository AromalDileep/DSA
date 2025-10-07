class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort first to handle duplicates easily

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicates on the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # i+1 since each number can be used once
                path.pop()

        backtrack(0, [], 0)
        return res

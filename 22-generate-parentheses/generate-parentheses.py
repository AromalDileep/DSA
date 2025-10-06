class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open_count, close_count):
            # base case: if length == 2 * n, add to result
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # condition 1: we can add '(' if open_count < n
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # condition 2: we can add ')' if close_count < open_count
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res

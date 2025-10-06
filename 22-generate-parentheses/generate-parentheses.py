class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # Add '(' if we still have some left
            if open_count < n:
                path.append("(")               # add '('
                backtrack(path, open_count + 1, close_count)
                path.pop()                     # remove '(' after recursion

            # Add ')' if it won't exceed the number of '('
            if close_count < open_count:
                path.append(")")               # add ')'
                backtrack(path, open_count, close_count + 1)
                path.pop()                     # remove ')' after recursion

        backtrack([], 0, 0)
        return res

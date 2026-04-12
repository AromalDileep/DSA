class Solution:
    def minimumDistance(self, word: str) -> int:

        memo = {}

        def dp(si, f1, f2):

            if si == len(word):
                return 0

            # check cache
            if (si, f1, f2) in memo:
                return memo[(si, f1, f2)]

            c = word[si]
            pos = ord(c) - ord("A")
            i, j = pos // 6, pos % 6

            distance1 = 0 if f1 == (-1, -1) else abs(f1[0]-i) + abs(f1[1]-j)
            cost1 = distance1 + dp(si+1, (i, j), f2)

            distance2 = 0 if f2 == (-1, -1) else abs(f2[0]-i) + abs(f2[1]-j)
            cost2 = distance2 + dp(si+1, f1, (i, j))

            best = min(cost1, cost2)

            # store result
            memo[(si, f1, f2)] = best

            return best

        return dp(0, (-1, -1), (-1, -1))

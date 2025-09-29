class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        
        for length in range(2, n):  # length of subpolygon
            for i in range(n-length):
                j = i + length
                dp[i][j] = min(
                    dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    for k in range(i+1, j)
                )
        print(dp)
        return dp[0][n-1]

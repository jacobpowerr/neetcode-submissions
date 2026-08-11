class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        
        dp = [[0] * n for _ in range(m)]

        for c in range(n-1):
            dp[m-1][c] = 1

        for r in range(m-1):
            dp[r][n-1] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]

        return dp[0][0]
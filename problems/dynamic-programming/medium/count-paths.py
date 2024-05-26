# Can be brute forced with O(2^(M + N)) time efficiency
# DP is dp[m][n] = dp[m - 1][n] + dp[m][n  -1]
# Yay didn't time myself but prob took <20 minutes for my first medium 2D DP problem
# 53% runtime, 99.6% memory
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        dp = [[1] * n] * m
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp [r][c - 1]

        return dp[m - 1][n - 1]

sln = Solution()
print(sln.uniquePaths(3, 6))
print(sln.uniquePaths(3, 3))

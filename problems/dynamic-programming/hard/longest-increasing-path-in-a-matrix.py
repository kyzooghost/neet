# Found visited cell - add to current path

# 70% runtime, 74% memory, 30 minutes
# Not pleased with this one - this is labelled as a hard but I feel this is a standard medium matrix problem
# Expect myself to do this one in under 20 minutes at most
# Had the correct idea straight away, but kept getting messed up in edge cases and implementation
#   LESSON #1 - When you are recursively computing path length (or binary tree height) - you return `1 + dfs()`, You also don't need to pass the path length
#   LESSON #2 - Wrong assumption that cell value is > 0, when it is >= 0
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.resp = float("-inf")
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, last_number):
            # Out of bounds
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0
            # Not increasing path
            if matrix[row][col] <= last_number:
                return 0
            # Seen in dp
            if dp[row][col] > -1:
                return dp[row][col]
            p1 = dfs(row + 1, col, matrix[row][col])
            p2 = dfs(row - 1, col, matrix[row][col])
            p3 = dfs(row, col + 1, matrix[row][col])
            p4 = dfs(row, col - 1, matrix[row][col])

            dp[row][col] = 1 + max(p1, p2, p3, p4)
            self.resp = max(self.resp, dp[row][col])
            return dp[row][col]

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, -1)

        return self.resp

sln = Solution()
# print(sln.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
# print(sln.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
# print(sln.longestIncreasingPath([[1]]))
print(sln.longestIncreasingPath([[7,7,5],[2,4,6],[8,2,0]]))
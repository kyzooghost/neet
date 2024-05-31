# 51% runtime, 46% memory
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        resp = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if visited[r][c]: return 0
            visited[r][c] = True
            if grid[r][c] == 0: return 0
            # Expect to be 1 here
            sum = grid[r][c]
            sum += dfs(r + 1, c)
            sum += dfs(r - 1, c)
            sum += dfs(r, c+1)
            sum += dfs(r, c-1)
            return sum

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    resp = max(resp, dfs(r, c))
        
        return resp

sln = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sln.maxAreaOfIsland(grid))
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# 10% runtime, 15% memory
# BFS is a bit meh, rather do recursive DFS with base cases at the start of the function
class Solution_Neet(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        height, width = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(y, x):
            q = collections.deque()
            visited.add((y, x))
            q.append((y, x))
            while q:
                cur_y, cur_x = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for y_diff, x_diff in directions:
                    new_y, new_x = cur_y + y_diff, cur_x + x_diff
                    if new_y not in range(height):
                        continue
                    if new_x not in range(width):
                        continue
                    if grid[new_y][new_x] == "0":
                        continue
                    if (new_y, new_x) in visited:
                        continue
                    q.append((new_y, new_x))
                    visited.add((new_y, new_x))


        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1" and (y, x) not in visited:
                    bfs(y, x)
                    islands += 1
        
        return islands

# 38% runtime, 5% memory
# Easier version of word-search, sigh had the correct idea and implementation except thought we were dealing with int type and not str type
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.resp = 0
        self.visited = {}
        width, height = len(grid[0]), len(grid)

        def dfs(i, j):
            # Out of bounds
            if i < 0 or j < 0 or i >= width or j >= height:
                return

            # Water
            if grid[j][i] == "0":
                return
            
            # Already visited
            if (i, j) in self.visited:
                return

            self.visited[(i, j)] = True

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for y in range(height):
            for x in range(width):
                if (x, y) in self.visited:
                    continue
                if grid[y][x] == "0":
                    continue
                dfs(x, y)
                self.resp += 1

        return self.resp
    
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
sln = Solution()
print(sln.numIslands(grid))
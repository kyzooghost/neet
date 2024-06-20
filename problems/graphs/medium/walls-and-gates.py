# Each land cell with distance to nearest treasure chest
# Probably easiest to DFS starting from each treasure chest, and fill in the cells
# Also should be able to do this in-place

from collections import deque

# Ok, O(E) solution because we will not revisit nodes 
class Solution_BFS:
    def islandsAndTreasure(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: queue.append((r, c))

        cur_dist = 1
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                (r, c) = queue.popleft()
                next_arr = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                
                for next_r, next_c in next_arr:
                    if next_r < 0 or next_c < 0 or next_r >= rows or next_c >= cols: continue
                    # Either already visited, or treasure or water
                    if grid[next_r][next_c] <= rows * cols: continue
                    grid[next_r][next_c] = cur_dist
                    queue.append((next_r, next_c))
            
            cur_dist += 1

        return grid

# Yay got a solution in 12 minutes, no % because is a premium problem
# Hmm this is DFS, so even though it is optimized it is still worst cast O(E^2)
class Solution:
    def islandsAndTreasure(self, grid):
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, dist):
            # Out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols: return
            # Treasure chest or water
            if grid[r][c] < 0: return
            # Already has closer treasure chest
            if dist > grid[r][c]: return
            else:
                grid[r][c] = dist
                dfs(r + 1, c, dist + 1)
                dfs(r - 1, c, dist + 1)
                dfs(r, c + 1, dist + 1)
                dfs(r, c - 1, dist + 1)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: dfs(r, c, 0)

        return grid

sln = Solution()
g = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
print(sln.islandsAndTreasure(g))
# print(sln.islandsAndTreasure())
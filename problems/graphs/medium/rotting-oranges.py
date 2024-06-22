from collections import deque

# This should be BFS from each rotting orange
# Count how many oranges have been rotten at the end
# 0 -> empty, 1 -> fresh, 2 -> rotten

# Yay first successful submission in just under 15 minutes - 89% runtime and 73% memory
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: fresh_count += 1
                if grid[r][c] == 2: queue.append((r,c))
        
        resp = 0
        while queue:
            # No fresh oranges -> done
            if fresh_count == 0: break

            resp += 1
            queue_len = len(queue)
            for _ in range(queue_len):
                (r, c) = queue.popleft()
                new_cells = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for new_r, new_c in new_cells:
                    # Out of bounds
                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols: continue
                    # New rot
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh_count -= 1
                        queue.append((new_r, new_c))
        
        # Fresh orange remaining
        if fresh_count > 0: return -1
        return resp

sln = Solution()
print(sln.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(sln.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(sln.orangesRotting([[0,2]]))

# print(sln.orangesRotting())
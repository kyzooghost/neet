# Hmm this is finding the route from corner-to-corner, with the lowest possible elevation
# Each grid value is unique, and grid values must be between 0 and n^2
# Must be a square
# Min value is max of either corner

from heapq import heappush, heappop

class Solution_Neet(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# 54% runtime, 72% memory
# Heap value = max height encountered, rather than grid value itself
class Solution_V3(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # (max_node_encountered, i, j)
        min_queue = []
        visited = {}
        heappush(min_queue, (grid[0][0], 0, 0))

        def walk_node(i, j, prev_max):
            if i < 0 or j < 0 or i > n - 1 or j > n - 1: return
            if (i, j) in visited: return
            max_node_encountered = max(grid[i][j], prev_max)
            heappush(min_queue, (max_node_encountered, i, j))

        while min_queue:
            val, i, j = heappop(min_queue)
            # This modification improves time efficieny to 64%
            if i == n - 1 and j == n - 1: return val
            if (i, j) in visited: continue
            visited[(i, j)] = True

            # Look at each adjacent node, update min_queue
            walk_node(i+1,j,val)
            walk_node(i-1,j,val)
            walk_node(i,j+1,val)
            walk_node(i,j-1,val)

# Ok the hint is also saying try Djikstra - O(V + E log V), iterate through every edge using min-queue of nodes
# So Djikstra's is BFS using min-queue, maintaining SPT
# O(N^2 log N^2)
# We want something else instead of SPT here - max node encountered, and we want to minimise it
# Oh but this got 34% runtime, 40% memory, took another 30 minutes but had to reference previous Djikstra implementation
class Solution_V2(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        max_node_encountered_matrix = [[float("inf") for _ in range(n)] for _ in range(n)]
        max_node_encountered_matrix[0][0] = grid[0][0]
        # (val, i, j)
        min_queue = []
        visited = set()
        heappush(min_queue, (grid[0][0], 0, 0))

        def walk_node(i, j, prev_max):
            if i < 0 or j < 0 or i > n - 1 or j > n - 1: return
            val = grid[i][j]
            if val in visited: return
            max_node_encountered_matrix[i][j] = min(max_node_encountered_matrix[i][j], max(val, prev_max))
            heappush(min_queue, (val, i, j))

        while min_queue:
            val, i, j = heappop(min_queue)
            # This modification improves time efficieny to 64%
            if i == n - 1 and j == n - 1: return max_node_encountered_matrix[n - 1][n - 1]
            if val in visited: continue
            visited.add(val)

            # Look at each adjacent node, updat spt + min_queue
            prev_max = max_node_encountered_matrix[i][j]
            walk_node(i+1,j,prev_max)
            walk_node(i-1,j,prev_max)
            walk_node(i,j+1,prev_max)
            walk_node(i,j-1,prev_max)
        
        return max_node_encountered_matrix[n - 1][n - 1]


# A brute force way is to increment from 0 to n^2, and find the lowest value that you can DFS from corner-to-corner. This is O(N^3) time complexity
# Dang the hint is telling us to use binary search for this instead, so O(N^2 * lg N)
# Alright, binary search approach gives 11% runtime, 8% memory. Solved in 36 mins but saw hint at 22 mins.
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        visited = set()

        def dfs(i, j, depth):
            # Out of bounds
            if i < 0 or j < 0 or i > n - 1 or j > n - 1:
                return False
            
            val = grid[i][j]
            # Cannot reach
            if val > depth:
                return False
            # Reached other corner
            if i == n - 1 and j == n - 1:
                return True
            # Visited
            if val in visited:
                return False
            
            visited.add(val)
            r1 = dfs(i + 1, j, depth)
            r2 = dfs(i - 1, j, depth)
            r3 = dfs(i, j + 1, depth)
            r4 = dfs(i, j - 1, depth)
            return r1 or r2 or r3 or r4
        
        # Binary search
        l, r = 0, (n * n) - 1
        resp = r

        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            visited.clear()
            dfs_resp = dfs(0, 0, mid)
            # Found, try smaller
            if dfs_resp:
                resp = min(resp, mid)
                r = mid
            # Not found, try bigger
            else:
                l = mid + 1
        
        return resp




        # visited = set()
        # n = len(grid)

        # def dfs(i, j, cur_max):
        #     # Out of bounds
        #     if i < 0 or j < 0 or i > n - 1 or j > n - 1:
        #         return 0
            
        #     val = grid[i][j]
        #     new_max = max(cur_max, val)
        #     # Reached other corner
        #     if i == n - 1 and j == n - 1:
        #         return new_max
        #     # visited
        #     if val in visited:
        #         return 0
        #     # Make use of unique values in each grid square
        #     visited.add(val)
            
        #     r1 = dfs(i + 1, j, new_max)
        #     if r1 != 0: return r1
        #     r2 = dfs(i - 1, j, new_max)
        #     if r2 != 0: return r2
        #     r3 = dfs(i, j + 1, new_max)
        #     if r3 != 0: return r3
        #     r4 = dfs(i, j - 1, new_max)
        #     if r4 != 0: return r4



        # return dfs(0, 0)

sln = Solution_V2()
print(sln.swimInWater([[0,1],[2,3]]))

grid0 = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]]
print(sln.swimInWater(grid0))

grid1 = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(sln.swimInWater(grid1))

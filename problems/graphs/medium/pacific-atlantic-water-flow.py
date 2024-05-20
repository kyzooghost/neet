# 60% runtime, 77% memory
# Pretty nice problem actually
class Solution_Neet(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r,c) in visit: return
            if r < 0 or c < 0: return
            if r >= rows or c >= cols: return
            cur_height = heights[r][c]
            if cur_height < prevHeight: return
            visit.add((r, c))
            dfs(r + 1, c, visit, cur_height)
            dfs(r - 1, c, visit, cur_height)
            dfs(r, c + 1, visit, cur_height)
            dfs(r, c - 1, visit, cur_height)

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        resp = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    resp.append([r, c])
        return resp


# Gg, flipping the problem around and going from the water - O(MN) because only need to visit each cell at most twice
# 78% runtime, 9% memory
class Solution_AfterNeetVideo(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights), len(heights[0])
        self.pacific, self.atlantic = {}, {}
        
        def dfs_pacific(r, c, prev_height):
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if (r, c) in self.visited:
                return
            cur_height = heights[r][c]
            if cur_height < prev_height:
                return
            self.visited[(r, c)] = True
            self.pacific[(r, c)] = True

            dfs_pacific(r + 1, c, cur_height)
            dfs_pacific(r - 1, c, cur_height)
            dfs_pacific(r, c + 1, cur_height)
            dfs_pacific(r, c - 1, cur_height)

        def dfs_atlantic(r, c, prev_height):
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if (r, c) in self.visited:
                return
            cur_height = heights[r][c]
            if cur_height < prev_height:
                return
            self.visited[(r, c)] = True
            self.atlantic[(r, c)] = True
            dfs_atlantic(r + 1, c, cur_height)
            dfs_atlantic(r - 1, c, cur_height)
            dfs_atlantic(r, c + 1, cur_height)
            dfs_atlantic(r, c - 1, cur_height)
            
        # First row + col -> Pacific
        self.visited = {}
        for c in range(cols):
            dfs_pacific(0, c, float("-inf"))
        for r in range(rows):
            dfs_pacific(r, 0, float("-inf"))

        # Last row + col -> Atlantic
        self.visited = {}
        for c in range(cols):
            dfs_atlantic(rows - 1, c, float("-inf"))
        for r in range(rows):
            dfs_atlantic(r, cols - 1, float("-inf"))

        # Iterate through results, find which results are in both oceans
        resp = []
        for (r, c) in self.pacific.keys():
            if (r, c) in self.atlantic:
                resp.append([r, c])

        return resp


# 10% runtime, 15% memory
# Urgh I had the idea and core implementation down in <15 minutes, but I got messed up in the order of DFS conditions for a whole train ride (~23 minutes)
# The only difference between the final implementation and the initial submission is that I swapped the positions of the 'higher height' check and marking self.visited
# Yes it is premature to mark self.visited before running 'higher height' check - because you can visit the same node from multiple directions
# Worst case O (M^2 N^2)
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.resp = []
        rows, cols = len(heights), len(heights[0])
        self.visited = {}
        self.pacific, self.atlantic = {}, {}

        def dfs(r, c, orig_r, orig_c, prev_height):
            # Out of bounds - Pacific
            if r < 0 or c < 0:
                self.pacific[(orig_r, orig_c)] = True
                return
            # Out of bounds - Atlantic
            if r >= rows or c >= cols:
                self.atlantic[(orig_r, orig_c)] = True
                return
            # Visited in this DFS
            if (r, c) in self.visited:
                return
            # Higher height
            cur_height = heights[r][c]
            if cur_height > prev_height:
                return

            # Mark visited
            self.visited[(r, c)] = True

            # Already found result from previous DFS, can inherit result
            is_pacific = (r, c) in self.pacific
            is_atlantic = (r, c) in self.atlantic
            if is_pacific:
                self.pacific[(orig_r, orig_c)] = True
            if is_atlantic:
                self.atlantic[(orig_r, orig_c)] = True
            if is_pacific or is_atlantic:
                return

            dfs(r + 1, c, orig_r, orig_c, cur_height)
            dfs(r - 1, c, orig_r, orig_c, cur_height)
            dfs(r, c + 1, orig_r, orig_c, cur_height)
            dfs(r, c - 1, orig_r, orig_c, cur_height)

        # DFS from each node
        for row in range(rows):
            for col in range(cols):
                self.visited = {}
                dfs(row, col, row, col, float("inf"))

        # Iterate through results, find which results are in both oceans
        for (r, c) in self.pacific.keys():
            if (r, c) in self.atlantic:
                self.resp.append([r, c])

        return self.resp
    

heights = [
    [8,13,11,18,14,16,16,4,4,8,10,11,1,19,7],
    [2,9,15,16,14,5,8,15,9,5,14,6,10,15,5],
    [15,16,17,10,3,6,3,4,2,17,0,12,4,1,3],
    [13,6,13,15,15,16,4,10,7,4,19,19,4,9,13],
    [7,1,9,14,9,11,5,4,15,19,6,0,0,13,5],
    [9,9,15,12,15,5,1,1,18,1,2,16,15,18,9],
    [13,0,4,18,12,0,11,0,1,15,1,15,4,2,0],
    [11,13,12,16,9,18,6,8,18,1,5,12,17,13,5],
    [7,17,2,5,0,17,9,18,4,13,6,13,7,2,1],
    [2,3,9,0,19,6,6,15,14,4,8,1,19,5,9],
    [3,10,5,11,7,14,1,5,3,19,12,5,2,13,16],
    [0,8,10,18,17,5,5,8,2,11,5,16,4,9,14],
    [15,9,16,18,9,5,2,5,13,3,10,19,9,14,3],
    [12,11,16,1,10,12,6,18,6,6,18,10,9,5,2],
    [17,9,6,6,14,9,2,2,13,13,15,17,15,3,14],
    [18,14,12,6,18,16,4,10,19,5,6,8,9,1,6]
]

heights2 = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,18],[63,120,121,122,123,124,125,126,127,128,129,130,131,132,133,80,19],[62,119,168,169,170,171,172,173,174,175,176,177,178,179,134,81,20],[61,118,167,208,209,210,211,212,213,214,215,216,217,180,135,82,21],[60,117,166,207,240,241,242,243,244,245,246,247,218,181,136,83,22],[59,116,165,206,239,264,265,266,267,268,269,248,219,182,137,84,23],[58,115,164,205,238,263,280,281,282,283,270,249,220,183,138,85,24],[57,114,163,204,237,262,279,288,289,284,271,250,221,184,139,86,25],[56,113,162,203,236,261,278,287,286,285,272,251,222,185,140,87,26],[55,112,161,202,235,260,277,276,275,274,273,252,223,186,141,88,27],[54,111,160,201,234,259,258,257,256,255,254,253,224,187,142,89,28],[53,110,159,200,233,232,231,230,229,228,227,226,225,188,143,90,29],[52,109,158,199,198,197,196,195,194,193,192,191,190,189,144,91,30],[51,108,157,156,155,154,153,152,151,150,149,148,147,146,145,92,31],[50,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,32],[49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33]]

heights3 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

# 80 - 18

# //[11, 3]
# [[0,14],[12,2],[15,0],[12,3],[13,2],[1,13],[13,1],[12,0],[0,13],[13,0],[14,0]]
# [[0,13],[0,14],[1,13],[11,3],[12,0],[12,2],[12,3],[13,0],[13,1],[13,2],[14,0],[15,0]]

sln = Solution_AfterNeetVideo()
print(sln.pacificAtlantic(heights))
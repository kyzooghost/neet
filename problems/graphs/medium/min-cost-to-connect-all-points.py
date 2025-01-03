# This should be finding min SPT from any node, and you find the sum of the edges
# But hmm...one way is to compute every possible edge (N^2 time complexity), then put it on a min heap and iterate until we have found a unique graph
# Can we do better, do we have to consider every edge?

# Hmm if we start at node 0, find the closest connection. Then repeat. I think this then becomes O(N) time complexity. Let's do that.
# No wait above is wrong, it is possible for node 0 to be the closest connection to all other nodes. So it is still O(N^2 time complexity)
# So just implement the first approach and see if we get TLE

# Hmm, where I am getting flummoxed is the # of connected components, I need a single connected graph at the end

from typing import List
from heapq import heappush, heappop

# Ahh, Prim's and Kruskal's algorithm from first minute of watching Neet's tutorial, yea I haven't touched those in years
# So Dijkstra's finds the shortest path between 2 vertices, but it does not produce the minimum spanning tree (MST). But with a minor change it can produce the MST.
# Ok so the 'minor change' is that you don't dump all the edges into the min heap, but the min heap represents the 'frontier' to your current tree
# That's the central concept really. Glad that we don't need to implement union find here, because I always forget union find unless I did it a few days ago.
# The other thing to note is that min_heap with O(N^2) elements => O(N^2 lg N) time complexity
# But lol, this is 39% runtime and 5% memory
class Solution_Neet:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        adjacency = {}
        last_visited = 0
        visited = set([0])
        frontier = []

        # Add every edge to min_heap
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjacency[(i, j)] = dist
                adjacency[(j, i)] = dist
        
        resp = 0
        # Create our MST
        while len(visited) < len(points):
            # Populate frontier
            for i in range(len(points)):
                if i in visited: continue
                dist = adjacency[(last_visited, i)]
                heappush(frontier, (dist, i))
                # print(f"added to frontier {last_visited}->{i} dist={dist}")

            dist, i = heappop(frontier)
            while i in visited:
                dist, i = heappop(frontier)
            visited.add(i)
            last_visited = i
            resp += dist
            # print(f"added to SPT node={i} dist={dist}")

        return resp

# Damn, took 49 minutes and copy-pasting the union-find implementation from another problem to get first pass on Neet
# But yay, same solution for 84% memory and 53% memory for Leetcode
# But urgh 49 minutes to get a first pass...getting really rusty at Leetcode
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        min_heap = []
        # Union find data structures
        # Each node starts as its own parent
        parent = [i for i in range(len(points))]
        size = [1 for i in range(len(points))]
        union_count = 0

        # Path compression - set parent[i] to recursive call
        def find_root(i):
            if parent[i] != i:
                parent[i] = find_root(parent[i])
            return parent[i]

        def union(i, j):
            # Already joined - no union
            root_i, root_j = find_root(i), find_root(j)
            if root_i == root_j:
                return 0
            
            # Merge smaller?
            if size[i] > size[j]:
                size[i] += size[j]
                # Change parent of root, not the current
                parent[root_j] = root_i
            else:
                size[j] += size[i]
                parent[root_i] = root_j

            return 1

        # Add every edge to min_heap
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # Possible optimization - just append to an array, then heapify the complete array after
                heappush(min_heap, (dist, i, j))

        resp = 0

        while union_count < len(points) - 1:
            dist, i, j = heappop(min_heap)
            # Possible optimization, duplicate `find_root(i) == find_root(j)` operation in union(), so just check result of union(i, j) for continuing
            if find_root(i) == find_root(j): continue
            union(i, j)
            union_count += 1
            resp += dist
        return resp

sln = Solution_Neet()
# print(sln.minCostConnectPoints())
# print(sln.minCostConnectPoints([[0,0]]))
print(sln.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]]))
print(sln.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sln.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))



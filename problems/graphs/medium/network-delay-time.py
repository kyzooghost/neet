from heapq import heappush, heappop

# Dijkstra -> Based on BFS using min-priority-queue
# Maintain spt[] - list of shortest paths to each node
# Start from node, visit each edge only once.
# Optimize time efficiency with visited
# Time complexity - E lg V - Iterate through each edge, min heap has worst-case size of V^2 - lg V^2 = 2 lg V
# E lg V^2 = 2 E lg V
class Solution_Neet(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

# This is a straightforward implementation of Dijkstra's algorithm
# 10% runtime, 39% memory without visited
# 26% runtime and 18% memory with visited
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        spt = [float("inf")] * (n + 1)
        spt[k] = 0
        edges = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for src, dst, time in times:
            edges[src][dst] = time
        
        min_queue = []
        visited = [False for _ in range(n + 1)]
        heappush(min_queue, (0, k))

        while min_queue:
            cur_dist, cur_node = heappop(min_queue)
            if visited[cur_node]: continue
            visited[cur_node] = True
            for dst_node in range(1, n+1):
                edge_dist = edges[cur_node][dst_node]
                if edge_dist >= 0:
                    spt[dst_node] = min(spt[dst_node], edge_dist + cur_dist)
                    heappush(min_queue, (spt[dst_node], dst_node))
                    edges[cur_node][dst_node] = -1
        resp = 0
        for i in range(1, n+1):
            if spt[i] == float("inf"): return -1
            resp = max(spt[i], resp)
        return resp
        

sln = Solution()
# print(sln.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# print(sln.networkDelayTime([[1,2,1]], 2, 1))
# print(sln.networkDelayTime([[1,2,1]], 2, 2))
# print(sln.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
print(sln.networkDelayTime(times, 5, 5))

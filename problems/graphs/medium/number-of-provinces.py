# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# 17% runtime, 40% memory - basically just union find
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        rows, cols = len(isConnected), len(isConnected[0])
        n = rows
        parent = [i for i in range(n)]
        size = [1] * n

        def find(n1):
            if parent[n1] != n1:
                parent[n1] = find(parent[n1])
            return parent[n1]

        # Size of orig changes, parent[root] changes
        # Want roots to merge, while 'size' is how high the subtree at n1 or n2 is
        def union(n1, n2):
            n1_root, n2_root = find(n1), find(n2)
            if n1_root == n2_root:
                return 0
            if size[n1] > size[n2]:
                size[n1] += size[n2]
                parent[n2_root] = n1_root
            else:
                size[n2] += size[n1]
                parent[n1_root] = n2_root

            return 1

        resp = n
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1:
                    resp -= union(r, c)

        return resp

# 2
a = [[1,1,0],[1,1,0],[0,0,1]]
# 3
b = [[1,0,0],[0,1,0],[0,0,1]]

sln = Solution()
print(sln.findCircleNum(a))
print(sln.findCircleNum(b))

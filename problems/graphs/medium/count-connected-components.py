from typing import List
from collections import defaultdict

# LC547

class Solution_Neet:
    # Alright union find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Each node starts as its own parent
        parent = [i for i in range(n)]
        # Tree height at each node
        size = [1] * n
        # O(N) space complexity for both these lists

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

        resp = n
        # At least O(E) time complexity. Lol Inverse Ackermann's time complexity
        for i, j in edges:
            resp -= union(i, j)
        return resp

# First submission was accepted :) Probably designed and implemented in <15 minutes
# I don't remember the union find algorithm, but this is essentially the same problem as 'number-of-islands'
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency dict for unidirected graph
        adjacency = defaultdict(list)
        for i, j in edges:
            adjacency[i].append(j)
            adjacency[j].append(i)

        self.visited = {}

        def dfs(n):
            self.visited[n] = True
            for i in adjacency.get(n, []):
                if i not in self.visited:
                    dfs(i)
            return 1

        # Each connected component can be traversed in a single DFS, so we are counting minimum DFS from external loop, to mark all nodes as visited
        resp = 0
        for i in range(n):
            if i not in self.visited:
                resp += dfs(i)
        return resp

sln = Solution()
sln2 = Solution_Neet()
# print(sln.countComponents(3, [[0,1], [0,2]]))
# print(sln2.countComponents(3, [[0,1], [0,2]]))
# print(sln.countComponents(6, [[0,1], [1,2], [2,3], [4,5]]))
# print(sln2.countComponents(6, [[0,1], [1,2], [2,3], [4,5]]))

print(sln2.countComponents(3, [[0,1], [0,2], [1,2]]))

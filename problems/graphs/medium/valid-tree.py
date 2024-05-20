from typing import List
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# What is a tree? 
# A cyclic graph cannot be a tree, but is that a good enough definition?
# A tree is where each node only has a single parent?
# You actual need both restrictions - no cycle, only single parent
# Multiple paths to a node == multiple direct parents hmm
# But also if cannot get to every node -> not a tree

# Alrighty, got an accepted solution in 32 minutes
# This problem is tough because the problem statement doesn't specify what are the requirements for a tree lol, you have work them out yourself
# 1. All nodes are connected, so DFS from single node will reach all nodes
# 2. There is only one path to a single node
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = {}

        # Undirected edges -> must consider both ways
        for i, j in edges:
            neighbors_i, neighbors_j = adjacency.get(i, []), adjacency.get(j, [])
            neighbors_i.append(j)
            neighbors_j.append(i)
            adjacency[i], adjacency[j] = neighbors_i, neighbors_j

        # return - is_not_tree
        def dfs(id):
            if id in self.visited:
                return True
            self.visited[id] = True
            for i in adjacency.get(id, []):
                forward_path = (id, i)
                reverse_path = (i, id)
                # If taken path before, skip - stop backtracking
                if forward_path in self.path or reverse_path in self.path:
                    pass
                # Take path
                else:
                    self.path[forward_path] = True
                    self.path[reverse_path] = True
                    if dfs(i): return True
            return False

        # Path store node walk done
        # So only need to do single walk
        self.visited, self.path = {},{}
        
        # Attempt DFS from single node
        if dfs(0): return False
        if len(self.visited) != n: return False
        
        return True
    
n = 5
edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
sln = Solution()
print(sln.validTree(n, edges1))
print(sln.validTree(n, edges2))
print(sln.validTree(4, [[0,1],[2,3]]))



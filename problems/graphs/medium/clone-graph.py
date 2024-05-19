# Yes DFS, but adjusted for the problem
# 19% runtime, 86% memory
# O(V + E) time complexity, O(V) space complexity
# Key is you don't want to DFS into a visited node, but you need to store the pointers to visited nodes

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        root = Node(node.val)
        self.visited = {}
        self.visited[node.val] = root

        def dfs(orig_node, clone_node):
            # No DFS into visited nodes

            for neighbor in orig_node.neighbors:
                if neighbor.val not in self.visited:
                    new_node = Node(neighbor.val)
                    self.visited[neighbor.val] = new_node
                    clone_node.neighbors.append(new_node)
                    dfs(neighbor, new_node)
                else:
                    new_node = self.visited[neighbor.val]
                    clone_node.neighbors.append(new_node)

        dfs(node, root)
        return root
        

# 75% runtime, 86% memory
# Same core ideas of i.) DFS and ii.) Store pointer to each new node
# Improvements - each dfs returns the original node. Store old -> new in a map

class Solution_Neet:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            else:
                new_node = Node(node.val)
                oldToNew[node] = new_node
                for neighbor in node.neighbors:
                    new_node.neighbors.append(dfs(neighbor))
                return new_node
        return dfs(node)
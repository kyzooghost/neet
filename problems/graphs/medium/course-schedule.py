class Solution_PythonicAfterNeet(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True

        adjacency = {}
        for i, j in prerequisites:
            neighbors = adjacency.get(j, [])
            neighbors.append(i)
            adjacency[j] = neighbors
        
        self.visited, self.path = {}, {}

        def dfs(course_id):
            self.visited[course_id] = True
            self.path[course_id] = True
            for i in adjacency.get(course_id, []):
                if i not in self.visited:
                    if dfs(i): return True
                elif i in self.path: return True

            del self.path[course_id]
            return False

        for course_id in range(numCourses):
            if course_id not in self.visited:
                if dfs(course_id): return False

        return True

class Solution_PostViewCycleAlgorithm(object):
    # Ok read Python code for https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
    # Seems like they keep two dicts - visited + cycle, visited change is never reverted, but cycle is. Hmm this looks like a time for space trade on my first implementation
    # Ok 84% runtime, 5% memory - Yea couldn't come up with find_cycle implementation from memory
    # Use visited to ensure DFS only visits each node only once - O(V + E), whereas if I revert visited than DFS will occur for every node and we are repeating steps
    # Use second cycle dict to store the current path - this will also enable us to return the cycle found if we need to
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        adjacency = {}
        for prerequisite in prerequisites:
            neighbors = adjacency.get(prerequisite[1], [])
            neighbors.append(prerequisite[0])
            adjacency[prerequisite[1]] = neighbors

        self.visited, self.path = {}, {}

        def dfs(node_id):
            self.visited[node_id] = True
            self.path[node_id] = True

            for neighbor_id in adjacency.get(node_id, []):
                # Only dfs if not already visited
                if neighbor_id not in self.visited:
                    cycle_found = dfs(neighbor_id)
                    if cycle_found == True:
                        return cycle_found
                # Else consider if will cause cycle
                elif neighbor_id in self.path:
                    return True

            del self.path[node_id]
            return False
        
        for course_id in range(numCourses):
            # No need to redo DFS for node
            if course_id not in self.visited:
                cycle_found = dfs(course_id)
                if cycle_found:
                    return False

        return True

class Solution(object):
    # Hmm this is topological sort, but I haven't implemented topological sort in Python before
    # When is topological sort impossible? A cycle
    # How can you detect a cycle? DFS
    # Mmm got to 48/52 cases passed with TLE...mmmmm. Main idea implemented in 15 minutes, debugged two test cases over the next 10 minutes
    # Still a brute force solution hmm - O(V * (V + E)) -> Doing DFS for each vertex
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # No restrictions -> Can take in any order
        if len(prerequisites) == 0:
            return True

        # Build adjacency list, then attempt to find cycle for each node
        adjacency = {}
        for prerequisite in prerequisites:
            neighbors = adjacency.get(prerequisite[1], [])
            neighbors.append(prerequisite[0])
            adjacency[prerequisite[1]] = neighbors

        def dfs(node_id):
            # Cycle found
            if node_id in self.visited:
                return True
            self.visited[node_id] = True
            for neighbor_id in adjacency.get(node_id, []):
                cycle_found = dfs(neighbor_id)
                if cycle_found == True:
                    return cycle_found
            del self.visited[node_id]
            return False

        for course_id in range(numCourses):
            self.visited = {}
            cycle_found = dfs(course_id)
            if cycle_found:
                return False

        return True
    
sln = Solution_PythonicAfterNeet()
print(sln.canFinish(2, [[1,0],[0,1]]))
print(sln.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))


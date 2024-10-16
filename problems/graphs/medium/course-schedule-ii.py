# [a <- b]
# Return ordering of courses to finish all
# If any valid answers, return any
# If impossible to finish all, return an empty

# Hmm the thing is that if a course may have no prequisites
# This means it can be a starting point
# This also means that i.) Any edge can go to it
# Any node with a prerequisite, cannot be a starting point
# Essentially you can DFS from every node, and attempt to find a path
# Ahh fuck, I missed this, 0->1->2 still fulfils the 0->2 prerequisite 
# So to go to 2, so need to iterate through all nodes and keep track of prerequisites
# Need to cross-off prerequisites if already got there

from collections import defaultdict

# Ahh damn, topological sort algorithm isn't what my mind was thinking
# In topological sort you DFS 'backwards' through dependencies.
# If you find cycle -> impossible
# If you find no more outgoing edges -> dependency-free node -> can add to resp
# Goddammit, 97% runtime and 32% memory. Yea the 'backwards' nature of topological sort is gg, that you append to resp at the end of the dfs call
class Solution_AfterNeet(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = defaultdict(list)

        for a, b in prerequisites:
            # b -> a is dependency, so edges go opposite way
            edges[a].append(b)

        resp = [] 
        visited = set()
        path = set()
        
        # return True if cycle found
        def dfs(node):
            if node in path: return True
            if node in visited: return False
            visited.add(node)
            path.add(node)

            for next_node in edges[node]:
                if dfs(next_node): return True

            resp.append(node)
            path.remove(node)
            return False

        for i in range(0, numCourses):
            # If cycle found, not possible
            if dfs(i): return []

        return resp

# Modify V3 such that you only visit each node once
# Fkkk, took me 2.5 hrs lol so bad for a Medium
# But yea, the TLE was from backtracking. There is no need to backtrack here.
# 5% Runtime, 6% memory
class Solution_V4(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        noPrequisiteNodes = set()
        hasPrequisitesSet = defaultdict(set)
        isPrerequisiteForDict = defaultdict(list)
        notVisited = set()

        for i in range(0, numCourses):
            noPrequisiteNodes.add(i)
            notVisited.add(i)
        
        for a, b in prerequisites:
            noPrequisiteNodes.discard(a)
            hasPrequisitesSet[a].add(b)
            isPrerequisiteForDict[b].append(a)

        if len(noPrequisiteNodes) == 0: return []
        resp = []

        def dfs(node):
            if node not in notVisited: return False
            if node in hasPrequisitesSet: return False

            for blocked_node in isPrerequisiteForDict[node]:
                hasPrequisitesSet[blocked_node].discard(node)
                if len(hasPrequisitesSet[blocked_node]) == 0: del hasPrequisitesSet[blocked_node]
            resp.append(node)
            notVisited.remove(node)

            # No more prerequisites left
            if len(resp) == numCourses: return True
            if len(hasPrequisitesSet) == 0: return True

            # Anything in hasPrequisitesSet is blocked
            # Iterate through any unblocked key of isPrerequisiteForDict
            for prerequisite in isPrerequisiteForDict:
                if prerequisite not in hasPrequisitesSet:
                    if dfs(prerequisite): return True

            return False
        
        # How do you know you have exhausted this path?

        for node in noPrequisiteNodes:
            if dfs(node): break
        
        if len(hasPrequisitesSet) > 0: return []
        elif len(resp) == 0: return resp
        else:
            for node in notVisited:
                resp.append(node)
            return resp

# Fek still TLE
# Hmm had a look at course-schedule-i, I guess you can let progress from 'one cycle' carry over to cycle. Don't need to start again from another noPrerequisiteNode
# Key is to ensure you only visit each node at most once I guess
class Solution_V3(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        noPrequisiteNodes = set()
        hasPrequisitesSet = defaultdict(set)
        isPrerequisiteForDict = defaultdict(list)
        notVisited = set()

        for i in range(0, numCourses):
            noPrequisiteNodes.add(i)
            notVisited.add(i)
        
        for a, b in prerequisites:
            noPrequisiteNodes.discard(a)
            hasPrequisitesSet[a].add(b)
            isPrerequisiteForDict[b].append(a)

        if len(noPrequisiteNodes) == 0: return []

        resp = []

        def dfs(node):
            if node not in notVisited: return False
            if node in hasPrequisitesSet: return False

            for blocked_node in isPrerequisiteForDict[node]:
                hasPrequisitesSet[blocked_node].discard(node)
                if len(hasPrequisitesSet[blocked_node]) == 0: del hasPrequisitesSet[blocked_node]
            resp.append(node)
            notVisited.remove(node)

            # No more prerequisites left
            if len(hasPrequisitesSet) == 0: return True

            # Anything in hasPrequisitesSet is blocked
            # Iterate through any unblocked key of isPrerequisiteForDict
            for prerequisite in isPrerequisiteForDict:
                if prerequisite not in hasPrequisitesSet:
                    if dfs(prerequisite): return True

            for blocked_node in isPrerequisiteForDict[node]: hasPrequisitesSet[blocked_node].add(node)
            resp.pop()
            notVisited.add(node)
            return False
        
        for node in noPrequisiteNodes:
            if dfs(node): break
        
        if len(resp) == 0: return resp
        else:
            for node in notVisited:
                resp.append(node)
            return resp

# Hmm still TLE hmmm
# Actually if you have no more prequisites then you are done. The remaining nodes can be done in any order.
# Still TLE hmm
# The implication of above is that you should prioritize looking for prerequisites, once prerequisites done you are finished
# Also if you can cut some lines if you return True for prerequisite fulfilled from the dfs
class Solution_V2(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        noPrequisiteNodes = set()
        # hasPrequisitesDict[a] -> What prequisites for a
        hasPrequisitesSet = defaultdict(set)
        # isPrerequisiteForDict[a] -> What is a prerequisite for
        isPrerequisiteForDict = defaultdict(list)
        notVisited = set()

        for i in range(0, numCourses):
            noPrequisiteNodes.add(i)
            notVisited.add(i)
        
        for a, b in prerequisites:
            noPrequisiteNodes.discard(a)
            hasPrequisitesSet[a].add(b)
            isPrerequisiteForDict[b].append(a)
        
        # No noPrequisiteNodes -> no possible starting point
        if len(noPrequisiteNodes) == 0: return []

        def dfs(node, resp, notVisited):
            # Found a full path, early return
            if len(resp) == numCourses: return
            # Already visited
            if node not in notVisited: return
            # Prerequisite not met, return
            if len(hasPrequisitesSet[node]) > 0: return

            # Remove from prequisites
            for blocked_node in isPrerequisiteForDict[node]:
                hasPrequisitesSet[blocked_node].discard(node)
                if len(hasPrequisitesSet[blocked_node]) == 0: del hasPrequisitesSet[blocked_node]
            resp.append(node)
            notVisited.remove(node)
            if len(resp) == numCourses: return

            # If no more prequisites, early exit
            if len(hasPrequisitesSet) == 0:
                for next_node in notVisited:
                    resp.append(next_node)
                return

            # Iterate through every node
            for next_node in notVisited:
                dfs(next_node, resp, notVisited)
                if len(resp) == numCourses: return

            # Add back to prerequisites
            for blocked_node in isPrerequisiteForDict[node]:
                hasPrequisitesSet[blocked_node].add(node)
            resp.pop()
            notVisited.add(node)

        resp = []
        for node in noPrequisiteNodes:
            dfs(node, resp, notVisited)
            if len(resp) == numCourses: return resp
        return resp

# Damn, took like 1 hr with last half hr during meeting. 
# Got success on Neetcode
# But got TLE on Leetcode
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        noPrequisiteNodes = set()
        # hasPrequisitesDict[a] -> What prequisites for a
        hasPrequisitesSet = defaultdict(set)
        # isPrerequisiteForDict[a] -> What is a prerequisite for
        isPrerequisiteForDict = defaultdict(list)

        for i in range(0, numCourses):
            noPrequisiteNodes.add(i)
        
        for a, b in prerequisites:
            noPrequisiteNodes.discard(a)
            hasPrequisitesSet[a].add(b)
            isPrerequisiteForDict[b].append(a)
        
        # No noPrequisiteNodes -> no possible starting point
        if len(noPrequisiteNodes) == 0: return []

        # Don't mix noPrequisiteNodes with edges
        # Any node to go to noPrequisiteNodes, noPrequisiteNode can go anywhere 
        def dfs(node, resp, visited):
            # Found a full path, early return
            if len(resp) == numCourses: return
            # Already visited
            if node in visited: return
            # Prerequisite not met, return
            if len(hasPrequisitesSet[node]) > 0: return

            # Remove from prequisites
            for blocked_node in isPrerequisiteForDict[node]:
                hasPrequisitesSet[blocked_node].discard(node)

            resp.append(node)
            visited.add(node)
            if len(resp) == numCourses: return

            # Iterate through every node
            for next_node in range(0, numCourses):
                dfs(next_node, resp, visited)
                if len(resp) == numCourses: return

            # Add back to prequisites
            for blocked_node in isPrerequisiteForDict[node]:
                hasPrequisitesSet[blocked_node].add(node)
            resp.pop()
            visited.remove(node)

        # Attempt DFS starting from every noPrerequisiteNodes
        resp = []
        visited = set()

        for node in noPrequisiteNodes:
            dfs(node, resp, visited)
            if len(resp) == numCourses: return resp
        return resp
    
sln = Solution_AfterNeet()
print(sln.findOrder(1, []))
print(sln.findOrder(2, [[1,0]]))
print(sln.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(sln.findOrder(3, [[1,0],[1,2],[0,1]]))


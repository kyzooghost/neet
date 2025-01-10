# Duplicate points allowed, and treated as different points
# Query point -> count # of ways to choose three points such that three points + query point form an axis-aligned square with positive area
# Axis-aligned square -> edges are all the same length, and are either parallel or perpendicular to the x-axis and y-axis
# Point = [x,y]

# Count is the hard part, what is the appropriate data structure?
# For each point, must be able to form a horizontal and vertical edge.
# -> Any points with same x- or same y- coordinate?
# -> Any pair of edges with same length?
# -> If find matching pair of edges, then check if any points exist at the remaining corner

# key, value pair -> x->y, and visa versa
# Also need to be able to add duplicate points hmm

from typing import List
from collections import defaultdict

# Ok different algorithm - 1st consider each pair as a diagonal candidate, then see if the other 2 edges exist
# Yay got 44% runtime and 45% memory
class DetectSquares_Neet:
    def __init__(self):
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        self.pointCount[(x,y)] += 1
        
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        resp = 0
        added_points = list(self.pointCount.keys())
        for x_diag, y_diag in added_points:
            # Check that we are dealing with a diagonal point
            if x == x_diag or y == y_diag: continue
            if abs(x - x_diag) != abs(y - y_diag): continue
            # print(f"square = {x},{y} - {x},{y_diag} - {x_diag},{y_diag} - {x_diag},{y}")
            resp += self.pointCount[(x_diag, y_diag)] * self.pointCount[(x, y_diag)] * self.pointCount[(x_diag, y)]
        return resp


# Ok great, got 83% runtime and 20% memory
class DetectSquares2:
    def __init__(self):
        self.xToY = defaultdict(set)
        self.yToX = defaultdict(set)
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        self.xToY[x].add(y)
        self.yToX[y].add(x)
        self.pointCount[(x,y)] += 1
        
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        resp = 0

        # Find x-match - O(N), store y-coord
        dist_to_x_match = defaultdict(list)
        for y_other in self.xToY[x]:
            if y == y_other: continue
            dist = abs(y - y_other)
            dist_to_x_match[dist].append(y_other)
        if len(dist_to_x_match.keys()) == 0: return 0
        
        # Find y-match - O(N), store x-coord
        dist_to_y_match = defaultdict(list)
        for x_other in self.yToX[y]:
            if x == x_other: continue
            dist = abs(x - x_other)
            dist_to_y_match[dist].append((x_other))
        if len(dist_to_y_match.keys()) == 0: return 0

        # Find if matching pair of edges
        last_corner_candidates = []
        for dist in dist_to_x_match.keys():
            if dist in dist_to_y_match:
                # Matching dist -> compute 4th point
                # Pair each point in x_match to each point in y_match
                for y_other in dist_to_x_match[dist]:
                    for x_other in dist_to_y_match[dist]:
                        count_1 = self.pointCount[(x, y_other)]
                        count_2 = self.pointCount[(x_other, y)]
                        last_corner_candidates.append((x_other, y_other, count_1 * count_2))
        if len(last_corner_candidates) == 0: return 0
        
        # Find if 4th corner exists
        for x_other, y_other, count in last_corner_candidates:
            resp += count * self.pointCount[(x_other, y_other)]

        return resp

# Fkkkk....took me 44 minutes to get passing case for Neetcode
# Ok same code passed for Leetcode at 5% runtime, 7% memory 
# Sigh so bad at Leetcode now...so slow and still got a shitty solution
# Ok let's see the performance characteristics - Yes O(1) add, but count is where it falls apart.
# I see O(N^3), and we should be able to make this more efficient by making use of combinatorics maths
class DetectSquares:
    def __init__(self):
        self.xToY = defaultdict(set)
        self.yToX = defaultdict(set)
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        self.xToY[x].add(y)
        self.yToX[y].add(x)
        self.pointCount[(x,y)] += 1
        
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        resp = 0

        # Find x-match - O(N), the inner-loop just 'uncompacts' the list
        dist_to_x_match = defaultdict(list)
        for y_other in self.xToY[x]:
            if y == y_other: continue
            for _ in range(self.pointCount[(x, y_other)]):
                dist = abs(y - y_other)
                dist_to_x_match[dist].append((x, y_other))
        if len(dist_to_x_match.keys()) == 0: return 0
        
        # Find y-match - O(N), the inner-loop just 'uncompacts' the list
        dist_to_y_match = defaultdict(list)
        for x_other in self.yToX[y]:
            if x == x_other: continue
            for _ in range(self.pointCount[(x_other, y)]):
                dist = abs(x - x_other)
                dist_to_y_match[dist].append((x_other, y))
        if len(dist_to_y_match.keys()) == 0: return 0

        # Find if matching pair of edges - Potentially O(N^3) here
        last_corner_candidates = []
        for dist in dist_to_x_match.keys():
            if dist in dist_to_y_match:
                # Matching dist -> compute 4th point
                # Pair each point in x_match to each point in y_match
                for _, y_other in dist_to_x_match[dist]:
                    for x_other, _ in dist_to_y_match[dist]:
                        last_corner_candidates.append((x_other, y_other))
        
        if len(last_corner_candidates) == 0: return 0
        
        # Find if 4th corner exists
        for x_other, y_other in last_corner_candidates:
            resp += self.pointCount[(x_other, y_other)]

        return resp

# Case 1
countSquares = DetectSquares_Neet()
countSquares.add([1, 1])
countSquares.add([2, 2])
countSquares.add([1, 2])
print(countSquares.count([2, 1])) #1
print(countSquares.count([3, 3])) #0
countSquares.add([2, 2])
print(countSquares.count([2, 1])) #2

# Case 2
countSquares = DetectSquares_Neet()
countSquares.add([5, 5])
countSquares.add([5, 6])
countSquares.add([6, 5])
countSquares.add([6, 6])
print(countSquares.count([7, 7])) #0
print(countSquares.count([5, 5])) #1
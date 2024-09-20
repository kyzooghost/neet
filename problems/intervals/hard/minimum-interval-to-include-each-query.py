# intervals[i] = [lefti, righti], righti is inclusive end
# size = righti - lefti + 1
# Smallest interval such that lefti <= queries[j] <= righti
# No interval exists, -1
# resp - size of smallest interval

from heapq import heappush, heappop

# Still 10% runtime, 81% memory
class Solution_AfterNeet(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort(key = lambda x: x[0])
        resp, i = {}, 0
        interval_heap = []
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                interval = intervals[i]
                heappush(interval_heap, (interval[1] - interval[0] + 1, interval[1]))
                i += 1
            
            while interval_heap:
                size, interval_right = interval_heap[0]
                # Eligible -> store in resp and go to next query
                if interval_right >= query:
                    # Get min eligible size
                    # Only care if minimum size is eligible
                    # Don't care about ineligible larger sizes, because we can remove later
                    resp[query] = size
                    break
                # Ineligible - remove
                else:
                    heappop(interval_heap)

            if query not in resp: resp[query] = -1

        return [resp[q] for q in queries]


# Hmm ok how can we make this more efficient
# I think the M in O(M*N) is unavoidable, so how can we do better than iterating through all intervals hmm
# Hint 1 - Is there a way to order the intervals and queries such that it takes less time to query?
# Hint 2 - Is there a way to add and remove intervals by going from the smallest query to the largest query to find the minimum size?
# Hmm...order the queries from smallest to largest? Hmm if we did that then we should be able to do a single pass through the sorted intervals actually
# So if we order both intervals and queries - O(M lg M + N lg N)
# Ok yay got it, 6% runtime, 96% memory, well took 1.5hrs to get here but satisfying to get a working solution by myself
class Solution_V2(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort(key = lambda x: x[0])
        resp = [-1 for _ in range(len(queries))]
        # Min heap of queries
        queries_heap = []
        for i in range(len(queries)):
            query = queries[i]
            heappush(queries_heap, (query, i))

        def get_size(interval):
            return interval[1] - interval[0] + 1

        interval_heap = []
        i = 0

        # Iterate through heap
        while queries_heap:
            query, query_i = heappop(queries_heap)

            # Add if left <= query
            while i < len(intervals) and intervals[i][0] <= query:
                interval = intervals[i]
                heappush(interval_heap, (get_size(interval), interval[1]))
                i += 1
            
            while interval_heap:
                neg_size, interval_right = interval_heap[0]
                # Eligible -> store in resp and go to next query
                if interval_right >= query:
                    # Get min eligible size
                    # Only care if minimum size is eligible
                    # Don't care about ineligible larger sizes, because we can remove later
                    resp[query_i] = neg_size
                    break
                # Ineligible - remove
                else:
                    heappop(interval_heap)

        return resp


# Need to know i.) Which interval contains query, ii.) Smallest such interval
# If we sort intervals - O(N lg N)
# Then we can iterate until left_i > query
# O(M * N), where N is # len(intervals), M is len(queries)
# Ok got passing Neetcode submission in 19 minutes
# TLE for Leetcode, 34/42 passing cases hehe
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # O(N lg N) - sorted by left_i
        intervals.sort(key = lambda x: x[0])
        resp = [-1 for _ in range(len(queries))]

        def get_size(interval):
            return interval[1] - interval[0] + 1
        
        # O(M) outer loop
        for i in range(len(queries)):
            # Iterate through sorted intervals, 
            j = 0
            min_size = float("inf")
            while j < len(intervals) and intervals[j][0] <= queries[i]:
                if intervals[j][1] >= queries[i]:
                    min_size = min(min_size, get_size(intervals[j]))
                j += 1
            if min_size != float("inf"): resp[i] = min_size
            
        return resp

sln = Solution_AfterNeet()
print(sln.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))
print(sln.minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))

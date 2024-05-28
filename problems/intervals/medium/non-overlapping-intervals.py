class Solution_Neet(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        resp, end = 0, intervals[0][1]

        for i in range(1, len(intervals)):
            # If overlap
            if intervals[i][0] < end:
                resp += 1
                end = min(end, intervals[i][1])
            # No overlap
            else:
                end = intervals[i][1]
        return resp


# Hmm...so [1,2] and [2,3] are non overlapping
# For each interval start, we want the minimum interval end
# Yay got a working solution in just under 20 minutes. Feels good after struggling with insert-new-interval and merge-intervals
# 45% runtime, 53% memory
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        resp = 0
        cur = intervals[0]
        for i in range(1, len(intervals)):
            # Find overlap -> greedy for first end
            if intervals[i][0] < cur[1]:
                resp += 1
                if cur[1] < intervals[i][1]:
                    continue
                else:
                    cur = intervals[i]
            # No overlap, next
            else:
                cur = intervals[i]

        return resp
    
sln = Solution_Neet()
print(sln.eraseOverlapIntervals([[1,2],[2,4],[1,4]]))
print(sln.eraseOverlapIntervals([[[1,2],[2,3]]]))
print(sln.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(sln.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(sln.eraseOverlapIntervals([[0,7],[1,2],[2,4]]))
print(sln.eraseOverlapIntervals([[0,3],[1,4],[2,5]]))



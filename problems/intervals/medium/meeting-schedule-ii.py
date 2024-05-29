from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
# Cool, O(N lg N) method to solve the problem
class Solution_AfterNeet:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        start, end = [], []
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()
        s, e, resp, meetings = 0, 0, 0, 0
        while s < len(start) and e < len(start):
            # New meeting start
            if start[s] < end[e]:
                s += 1
                meetings += 1
            # Meeting end
            elif end[e] <= start[s]:
                e += 1
                meetings -= 1
            resp = max(resp, meetings)
        return resp

# Thinking can we reuse the solution for non-overlapping-intervals
# Ok this does work, but worst case O(N^2)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key=lambda x: x.start)
        resp = 0
        # Collect overlapping intervals
        remaining = intervals

        while remaining:
            tmp = []
            cur = remaining[0]
            # If any overlapping, place into tmp
            for i in range(1, len(remaining)):
                # Overlap
                if remaining[i].start < cur.end:
                    # Greedy for earliest end
                    if remaining[i].end < cur.end:
                        cur = remaining[i]
                        tmp.append(cur)
                    else:
                        tmp.append(remaining[i])
                # No overlap
                else:
                    cur = remaining[i]
            remaining = tmp
            resp += 1

        return resp

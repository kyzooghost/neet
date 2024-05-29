from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

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

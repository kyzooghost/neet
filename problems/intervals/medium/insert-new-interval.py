# 0 <= intervals.length <= 1000
# newInterval.length == intervals[i].length == 2
# 0 <= start <= end <= 1000

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# 35% runtime, 92% memory
# Sighhhhh first two attempts failed miserably. The problem is straightforward, implementation is not because there are quite a few edge cases
# Had to refine the way I think about it
#   Pass = completely to right
#   Passed everything -> Append to end
#   Insert to left
#   Left extension
#   Right extension - no hit of next interval, merge into next interval, surpass next interval

class Solution_V3(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        orig_length = len(intervals)
        new_start, new_end, = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # Pass if completely to the right
            if end < new_start:
                continue
            # Insert new interval to the left
            if new_end < start:
                intervals.insert(i, newInterval)
                return intervals
            # Involves current interval 
            else:
                # Need left extension
                if new_start < start: intervals[i][0] = new_start
                
                # Need right extension
                if new_end > end:
                    j = i + 1
                    stack = []
                    while j < orig_length:
                        # To the left of new interval
                        if new_end < intervals[j][0]:
                            break
                        # Within new interval
                        elif new_end <= intervals[j][1]:
                            stack.append(j)
                            new_end = intervals[j][1]
                            break
                        # Past new interval
                        else:
                            stack.append(j)
                            j += 1
                    while stack:
                        intervals.pop(stack.pop())
                    intervals[i][1] = new_end

                return intervals

        # New interval to right of all existing intervals
        intervals.append(newInterval)
        return intervals

class Solution_V2(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        orig_length = len(intervals)
        if orig_length == 0: return [newInterval]
        new_start, new_end, = newInterval[0], newInterval[1]

        i = 0
        while i < orig_length:
            start, end = intervals[i][0], intervals[i][1]
            # Go to next
            print(start, end, new_start, new_end)
            if new_end < start:
                print("hi")
                continue
            # Extend left
            elif new_start < start and new_end <= end:
                intervals[i][0] = new_start
                return intervals
            # No extension required
            elif start <= new_start and new_end <= end:
                return intervals
            # Extend right
            elif start <= new_start and end < new_end:
                j = i + 1
                pop_stack = []
                while j < orig_length:
                    # Extend right, without hitting next start of next
                    if new_end < intervals[j][0]:
                        break
                    # Hit middle of j
                    elif new_end <= intervals[j][1]:
                        pop_stack.append(j)
                        new_end = intervals[j][1]
                    # Pass j
                    else:
                        pop_stack.append(j)
                    j += 1
                while pop_stack:
                    intervals.pop(pop_stack.pop())
                intervals[i][1] = new_end
                return intervals
            # New_interval is superset of current
            elif new_start < start and end < new_end:
                intervals[i][0] = new_start
                j = i + 1
                pop_stack = []
                while j < orig_length:
                    # Extend right, without hitting next start of next
                    if new_end < intervals[j][0]:
                        break
                    # Hit middle of j
                    elif new_end <= intervals[j][1]:
                        pop_stack.append(j)
                        new_end = intervals[j][1]
                    # Pass j
                    else:
                        pop_stack.append(j)
                    j += 1
                while pop_stack:
                    intervals.pop(pop_stack.pop())

                intervals[i][1] = new_end
                return intervals

            # New interval to right
            else:
                # End of intervals
                if i == orig_length - 1:
                    break
                # Insert new interval
                elif new_end < intervals[i+1][0]:
                    intervals.insert(i, newInterval)
                # Else we are extending next interval

        # Reached end
        intervals.append(newInterval)
        return intervals

# Ok intervals are non-overlapping, and already sorted
# Case 1 - inside current interval, do nothing
# Case 2 - start in one interval, end in another -> merge intervals
# Case 3 - start outside one interval, end inside one (or visa versa) -> extend interval
# Case 4 - start between intervals -> Insert
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_start = newInterval[0]
        new_end = newInterval[1]
        original_length = len(intervals)
        if original_length == 0: return [newInterval]

        # Find start
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # Pass this interval
            if end < new_start:
                continue
            # Case 1 - inside current interval, do nothing
            elif start <= new_start and new_end <= end:
                break
            # Case 2 - start outside left, end inside -> extend current left
            elif new_start <= start and new_end <= end:
                intervals[i][0] = new_start
                break
            # Case 3 - new interval to the left
            elif new_start < start and new_end <= end:
                intervals.insert(i, newInterval)
                break
            # Case 4 - start inside, end outside
            else:
                # Case 4a - we are at the last interval
                if i == len(intervals) - 1:
                    intervals[i][1] = new_end
                # Case 4b - require merge with one of the next interval/s
                elif new_end >= intervals[i+1][0]:
                    j = i + 1
                    pop_stack = []
                    while j < original_length:
                        pop_stack.append(j)
                        if intervals[j][1] >= new_end:
                            intervals[i][1] = intervals[j][1]
                            break
                        j += 1
                    # If we didn't find a new interval
                    if intervals[i][1] == end: intervals[i][1] = new_end
                    while pop_stack:
                        intervals.pop(pop_stack.pop())
                else:
                    intervals[i][1] = new_end
                break

        return intervals

sln = Solution_V3()
print(sln.insert([[1,3],[4,6]],[2,5]))
print(sln.insert([[1,2],[3,5],[9,10]],[6,7]))
print(sln.insert([[1,3],[4,6]],[2,7]))
print(sln.insert([[1,3],[4,6]],[4,5]))
print(sln.insert([],[4,5]))
print(sln.insert([[1,5]],[1,7]))






# Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
# Output: [[1,6]]

# Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
# Output: [[1,2],[3,5],[6,7],[9,10]]
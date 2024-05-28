# Merge all overlapping intervals
# Return array of non-overlapping intervals
# No guarantee of sort

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Do we need to sort?
# No need to return sorted array
# How to use code from insert?
# Interval tree?
# Hmm, this is my issue - how to compare an unconsidered interval with all the present intervals
# I can only think of an O(N^2) implementation, where I build a new sorted list of intervals, and work out where to insert the new interval
# I'm blank for other implementations so let's just do it
# I can't fathom the logic to maintain an interval tree with non-overlapping intervals
# 5% runtime, 36.5% memory - mmm I think there has to be a better way to do this, I made so many errors with the insert-new-interval implementation mm...must be a simpler way
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        resp = [intervals[0]]

        # Loop to insert interval
        for i in range(1, len(intervals)):
            new_start, new_end = intervals[i][0], intervals[i][1]
            # print(resp, new_start, new_end)
            
            j = 0
            resp_length = len(resp)
            # Find place to insert, iterate through resp
            while j < resp_length:
                start, end = resp[j][0], resp[j][1]
                # To the right -> pass
                if end < new_start:
                    j += 1
                    continue
                # To the left -> insert and break
                elif new_end < start:
                    resp.insert(j, intervals[i])
                    break
                # Need to extend current
                else:
                    # Left extension
                    if new_start < start:
                        resp[j][0] = new_start
                    
                    # Right extension
                    if end < new_end:
                        stack = []
                        k = j + 1
                        while k < resp_length:
                            # Left of next interval
                            if new_end < resp[k][0]:
                                break
                            # In next interval
                            elif new_end <= resp[k][1]:
                                stack.append(k)
                                new_end = resp[k][1]
                                break
                            # Extend past interval
                            else:
                                stack.append(k)
                                k += 1
                        while stack:
                            resp.pop(stack.pop())
                        resp[j][1] = new_end
                    break
            
            # Passed all -> append to end
            if j == resp_length: resp.append(intervals[i])

        return resp

sln = Solution()
# print(sln.merge([[1,3],[1,5],[6,7]]))
# print(sln.merge([[1,3],[2,6],[8,10],[15,18]]))
# print(sln.merge([[1,4],[4,5]]))
# print(sln.merge([[1,2],[2,3]]))

# print(sln.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))

print(sln.merge([[0,2],[2,3],[4,4],[0,1],[5,7],[4,5],[0,0]]))




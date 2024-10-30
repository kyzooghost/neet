# Partition string into max parts
# So that each letter appear at most once in each partition
# For each letter - get first and last occurence of it - O(N)
# Iterate through each letter, and find the biggest partition splits

# Damn styled with O(N) solution, mine is O(N^2) worst case
# 72% runtime, 14% memory
class Solution_AfterNeet(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {}
        for i in range(len(s)):
            char = s[i]
            last[char] = i
        resp = []
        size, end = 0, 0

        for i in range(len(s)):
            char_end = last[s[i]]
            
            size += 1
            end = max(end, char_end)
            
            if i == end:
                resp.append(size)
                size = 0
                
        return resp

# Ok 32 minutes to pass Neetcode cases
# And this got 92% runtime and 18% memory for Leetcode with Python3, but error on Python runtime
# I guess I had the solution concept in decent time, prob in <10 mins. But I was too slow with implementing 'interval insertion'.
# Urgh Python vs Python3 has different behaviour for `intervals = intervals[:i] + [start, end] + intervals[i:]`. Don't want to spend time debugging this difference, so will just use Python3 from now on
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        first, last = {}, {}

        for i in range(len(s)):
            char = s[i]

            if char not in first:
                first[char] = i
                last[char] = i
            else:
                last[char] = i

        intervals = []

        # Iterate through every letter
        for char in first:
            if not intervals: intervals.append([first[char], last[char]])
            else:
                for i in range(len(intervals)):
                    start = first[char]
                    end = last[char]
                    interval = intervals[i]
                    interval_start = interval[0]
                    interval_end = interval[1]

                    # Skip to next
                    if interval_end < start:
                        if i == len(intervals) - 1:
                            intervals.append([start, end])
                            break
                        else:
                            pass
                    # Insert new interval to the left, and break
                    elif end < interval_start:
                        intervals = intervals[:i] + [start, end] + intervals[i:]
                        break
                    # Pass, inside current interval
                    else:
                        intervals[i][0] = min(start, interval_start)
                        intervals[i][1] = max(end, interval_end)
                        break
                
        resp = []
        for interval in intervals:
            resp.append(interval[1] - interval[0] + 1)
        return resp

sln = Solution_AfterNeet()
# print(sln.partitionLabels("ababcbacadefegdehijhklij"))
# print(sln.partitionLabels("gtywtbcnow"))
print(sln.partitionLabels("xyxxyzbzbbisl"))

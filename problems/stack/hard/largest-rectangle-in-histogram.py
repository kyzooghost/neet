# Well 15% runtime, 19% memory, slightly better
# Don't need reverse sweep, just 'backwards extension'
# 46% runtime, 22% memory
class Solution_V3(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        resp = float("-inf")
        stack = []

        # Left pass
        for i in range(len(heights)):
            cur_i = i
            while stack and stack[-1][0] > heights[i]:
                height, popped_i = stack.pop()
                resp = max(height * (i - popped_i), resp)
                cur_i = popped_i
            stack.append((heights[i], cur_i))

        while stack:
            height, popped_i = stack.pop()
            resp = max(height * (len(heights) - popped_i), resp)
        return resp

# Well 15% runtime, 19% memory, slightly better
class Solution_V2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        resp = float("-inf")
        stack = []

        # Left pass
        for i in range(len(heights)):
            if not stack:
                stack.append((heights[i], i))
            else:
                cur_i = i
                while stack and stack[-1][0] > heights[i]:
                    height, popped_i = stack.pop()
                    resp = max(height * (i - popped_i), resp)
                    cur_i = popped_i
                stack.append((heights[i], cur_i))

        while stack:
            height, popped_i = stack.pop()
            resp = max(height * (len(heights) - popped_i), resp)

        # Right pass
        for i in range(len(heights) - 1, -1, -1):
            if not stack:
                stack.append((heights[i], i))
            else:
                cur_i = i
                while stack and stack[-1][0] > heights[i]:
                    height, popped_i = stack.pop()
                    resp = max(height * (popped_i - i), resp)
                    cur_i = popped_i
                stack.append((heights[i], cur_i))

        while stack:
            height, popped_i = stack.pop()
            resp = max(height * (popped_i), resp)

        return resp

# Hmm monotonically increasing stack with a twist
# You can't discard the next value, only the previous values
# Keep running track
# Find something lower -> pop
# Area bound by this h -> h * (i - i) when popped
# Wow, got a successful submission for a hard in 19 minutes, but 11% runtime and 5% memory hmmm
# But this is already O(N) time and O(N) space lol
# Is it any better if I just use one stack twice, rather than two stacks once
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        resp = float("-inf")
        stack, reverse_stack = [], []

        # Left pass
        for i in range(len(heights)):
            if not stack:
                stack.append((heights[i], i))
            else:
                cur_i = i
                while stack and stack[-1][0] > heights[i]:
                    height, popped_i = stack.pop()
                    resp = max(height * (i - popped_i), resp)
                    cur_i = popped_i
                stack.append((heights[i], cur_i))

            reverse_i = len(heights) - i - 1
            if not reverse_stack:
                reverse_stack.append((heights[reverse_i], reverse_i))
            else:
                cur_reverse_i = reverse_i
                while reverse_stack and reverse_stack[-1][0] > heights[reverse_i]:
                    height, popped_i = reverse_stack.pop()
                    resp = max(height * (popped_i - reverse_i), resp)
                    cur_reverse_i = popped_i
                reverse_stack.append((heights[reverse_i], cur_reverse_i))

        while stack:
            height, popped_i = stack.pop()
            resp = max(height * (len(heights) - popped_i), resp)

        while reverse_stack:
            height, popped_i = reverse_stack.pop()
            resp = max(height * (popped_i + 1), resp)

        return resp

sln = Solution()
print(sln.largestRectangleArea([2,1,5,6,2,3]))
print(sln.largestRectangleArea([2,4]))
print(sln.largestRectangleArea([7,1,7,2,2,4]))



from collections import deque

# Cleaned up a bit because if you reorder the operations, you don't need to account for queue existence
class Solution_AfterNeet(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        resp = []
        queue = deque([])

        for i in range(len(nums)):
            # Should we popright?
            while queue and nums[i] > queue[-1][0]:
                queue.pop()
            # Will always append
            queue.append((nums[i], i))
            # Popleft if exceed
            if queue[0][1] < i - k + 1:
                queue.popleft()
            if i >= k - 1:
                resp.append(queue[0][0])
        
        return resp

# Deque??? That is not the same size as the window? Hmm haven't used a deque solution before. What would the deque represent at each position?
# Alright had some more time to think about it, we use a monotonic decreasing stack where the max element is at the head, and this is what we append to resp
# 26% runtime, 45% memory
# Eih this was pretty hard, mulled over this for a few hrs at least. I haven't used a deque in a solution before. Needed both pop() and popleft() for this solution. 
# I haven't implemented a monotonically decreasing queue before either
# I can see this being a practical problem - maintaining the max value of a stream
class Solution_V2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        resp = []
        queue = deque([])

        for i in range(len(nums)):
            if not queue:
                queue.append((nums[i], i))
            else:
                # Remove if out-of-index
                _, dequeue_head_i = queue[0]
                if dequeue_head_i < i - k + 1:
                    queue.popleft()

                # Maintain monotonically decreasing - using deque
                while queue and nums[i] > queue[-1][0]:
                    queue.pop()

                queue.append((nums[i], i))

            if i >= k - 1:
                resp.append(queue[0][0])
        return resp

sln = Solution_AfterNeet()
print(sln.maxSlidingWindow([1,2,1,0,4,2,6], 3))
print(sln.maxSlidingWindow([1,-1], 1))
print(sln.maxSlidingWindow([1,3,1,2,0,5], 3)) #[3,3,2,5]

# Not sure how this is a hard question, and it's such a weird question too
# Return an array, that has the max of each sliding window?
# O(K) space, worst case O(KN)...just an optimized brute force
# Hehe got TLE and passed 45/51 cases. Ok got an optimised brute force in just under 20 minutes.
# How can we optimise this hmm.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        resp = []
        # Find max for first sliding window
        cur_left = nums[0]
        cur_max = float("-inf")
        for i in range(k):
            cur_max = max(cur_max, nums[i])
        resp.append(cur_max)
        # Find max for next sliding windows
        for i in range(k, len(nums)):
            # Didn't lose last max
            if cur_left != cur_max:
                cur_max = max(cur_max, nums[i])
            # Else lost last max, reiterate
            else:
                cur_max = float("-inf")
                for j in range(i - k + 1, i + 1):
                    cur_max = max(cur_max, nums[j])
            cur_left = nums[i - k + 1]
            resp.append(cur_max)

        return resp
        

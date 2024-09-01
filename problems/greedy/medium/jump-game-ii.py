# Min number to reach end
# Start at num[0]

# max queue at each step
# try for biggest possible jump
# if fail, go for next biggest

# 39% runtime, 48% memory
class Solution_Neet(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            new_r = 0
            for i in range(l, r + 1):
                new_r = max(new_r, i + nums[i])
            l = r + 1
            r = new_r
            res += 1

        return res

# Still 28% runtime, 8% memory mmm
# After watching Neet too
class Solution_V3(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        arr = [float("inf") for _ in range(len(nums))]
        arr[0] = 0

        for i in range(len(nums)):
            next_i = i + nums[i]
            if next_i >= len(nums) - 1: return arr[i] + 1

            while next_i > i:
                if arr[next_i] != float("inf"): break
                arr[next_i] = arr[i] + 1
                next_i -= 1

# What if we start from the back, and scan the array to find the biggest possible jump
# Wow, works but less efficient than previously - 19% runtime, 5% memory
# This is an O(N^2) solution however
class Solution_V2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0

        def jump_back(i, step):
            if i == 0: return step
            j = 0
            while j < i:
                if j + nums[j] >= i: return jump_back(j, step + 1)
                j += 1

        return jump_back(len(nums) - 1, 0)

# [1,2,1,1,1]

# First successful submission for Neetcode at 21:38
# Lol successful for Leetcode, but 28% runtime and 5% memory lmao
from heapq import heappush, heappop

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0

        def recurse(i, step):
            print(i, step)
            if i >= len(nums): return float("inf")

            # Max PQ of nums
            heap = []
            for j in range(1, nums[i] + 1):
                if i + j == len(nums) - 1: return step + 1
                heappush(heap, (-nums[i + j] - i - j, i + j))

            resp = float("inf")
            while heap:
                _, index = heappop(heap)
                resp = recurse(index, step + 1)
                if resp != float("inf"): return resp

            return resp

        return recurse(0, 0)

sln = Solution_V3()
# print(sln.jump([2,1,2,1,0]))
print(sln.jump([2,4,1,1,1,1]))
# print(sln.jump([1,2,1,1,1]))


#  1 <= nums.length <= 1000
# -10 <= nums[i] <= 10

from typing import List

# Styled by Neet solution again haha
# So O(1) memory, O(N) time
# Don't store 0s
# 5% runtime, 65% memory
class Solution_Neet:
    def maxProduct(self, nums: List[int]) -> int:
        resp = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            if num == 0:
                curMax, curMin = 1, 1
            
            tmp = curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num * tmp, num * curMin, num)
            print(curMin, curMax)
            resp = max(resp, curMax)

        return resp
# Hmm ok - so won't get trapped by 0s you multiply by 0
# Also curMax, curMin is always multiplied by the current value - so you won't register 1 into your resp. curMax can be negative
# I was trying to handle the 0, which made it so much trickier
# I had the correct core approach, but where did I get tripped up
    # curMax does not have to be a positive #, nor does curMin need to be a negative #
    # For 0, you can use 1 as the intermediate # and multiply by 0 for the result

sln = Solution_Neet()
# print(sln.maxProduct([2,3,-2,4]))
# print(sln.maxProduct([-2,0,-1]))
# print(sln.maxProduct([0,0]))
# print(sln.maxProduct([1,2,-3,4]))
# print(sln.maxProduct([-2,-1]))
print(sln.maxProduct([-2,0,2,3,6,-9,-7]))

# [-2,0,2,3,6,-9,-7]

# Ok let's give ourselves more time here and attempt DP
# So let's continue on the approach of memoizing, should get an O(N) solution then
# 30% runtine, 10% memory - Ok yay got a DP solution eventually, in maybe another 45 minutes. I think I must have overcomplicated something though, because this solution is way too 'finicky' to come up with in an interview
# And ok, I watched Neet - my solution is the same core concept as the video but I must have gotten stuck in the implementation
class Solution_V2:
    def maxProduct(self, nums: List[int]) -> int:
        resp = nums[0]
        # Max and min for subarray ending at i
        dp_max = [nums[0] if nums[0] > 0 else 0] * len(nums)
        dp_min = [nums[0] if nums[0] < 0 else 0] * len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp_max[i] = 0
                dp_min[i] = 0
                resp = max(resp, 0)
            elif nums[i] > 0:
                dp_max[i] = nums[i] if dp_max[i - 1] == 0 else nums[i] * dp_max[i - 1]
                dp_min[i] = 0 if dp_min[i - 1] == 0 else nums[i] * dp_min[i - 1]
                if dp_max[i] != 0: resp = max(resp, dp_max[i])
            else:
                dp_max[i] = 0 if dp_min[i - 1] == 0 else nums[i] * dp_min[i - 1]
                dp_min[i] = nums[i] if dp_max[i - 1] == 0 else nums[i] * dp_max[i - 1]
                if dp_max[i] != 0: resp = max(resp, dp_max[i])
        
        return resp

# [-2,0,2,3,6,-9, -7]
# [0, 0,2,3,6, 0,-7*]
# [-2,0,0,0,0,-9,-7 ]

# Ok fuck the DP for now, let's just implement the O(N^2) solution I can think of. Similar approach as for longest-palindromic-string
# Ok kept trying to think of a DP solution but couldn't work it out, so did a 'walking backwards' on each iteration solution
# Implemented in ~30 minutes
# TLE and passed 186/190 cases on Leetcode mm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        resp = nums[0]

        for i in range(1, len(nums)):
            running_product = nums[i]
            resp = max(running_product, resp)
            if running_product == 0:
                continue
            # Walk backwards until hit 0
            for j in range(i - 1, -1, -1):
                running_product *= nums[j]
                resp = max(running_product, resp)
                if running_product == 0:
                    break

        return resp
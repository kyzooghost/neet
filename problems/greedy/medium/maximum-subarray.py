# Ok I have a new idea for DP
# dp[n] is the max subarray you can make ending at n, it is either nums[n] itself, nums[n] + dp[n - 1]
# fkkkkkk finally got it, I must have tinkered with at least 4 approaches over 3+ hrs before I got it
#   1.) Attempt O(N) with min L-bound subarray, min R-bound subarray, had issues with crossover
#   2.) Attempt 1D DP where dp[n] = max subarray for nums[0:n], could not get this to work with the case [8,-19,5,-4,20]
#   3.) Attempt O(N log N) with min heap, choose max for L or R subarray given lowest number. But this algorithm doesn't work for the test case [-2,1,-3,4,-1,2,1,-5,4]
#   4.) Brute force O(N^2) - worked but TLE on 201/210 cases
# 33% runtime, 49% memory
# I also got thrown off by this being under a 'Greedy' category rather than DP, and I didn't consider DP until reading the Leetcode discussion
class Solution_DP(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        resp = nums[0]
        dp = resp
        for i in range(1, len(nums)):
            dp = max(nums[i], nums[i] + dp)
            resp = max(resp, dp)

        return resp

sln = Solution_DP()
# print(sln.maxSubArray([8,-19,5,-4,20]))
print(sln.maxSubArray([5,4,-1,7,8]))

# Urghhhhhhhhhhhhhhhhhh didn't get this question in hours, probably had like 10 failed submissions
# Sigh TLE, O(N^2) on 201/210 cases.
class Solution_BruteForce(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        resp = nums[0]
        for i in range(1, len(nums)):
            running_sum = nums[i]
            resp = max(resp, running_sum)
            for j in range(i-1, -1, -1):
                running_sum += nums[j]
                resp = max(resp, running_sum)
        return resp        
    

# print(sln.maxSubArray([8,-19,5,-4,20]))
# print(sln.maxSubArray([5,4,-1,7,8]))

# Alright I've spent a few hours yet haven't been able to get an O(N) implementation to pass
# Can we do this with 1D DP? If you have 2 elements - you either the N-1 solution, extend it, or take the N element by itself
# dp(N) = max(dp(n-1), dp(n+1) + n, n by itself)

# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1: return nums[0]
#         sum = 0
#         for i in range(len(nums)):
#             sum += nums[i]


#         # Find l_min
#         l_min, l, tmp = 0, 0, 0
#         for i in range(len(nums) - 1):
#             tmp += nums[i]
#             if tmp < l_min:
#                 l_min = tmp
#                 l = i + 1

#         # Find r_min
#         r_min, r, tmp = 0, len(nums) - 1, 0
#         for i in range(len(nums) - 1,0, -1):
#             tmp += nums[i]
#             if tmp < r_min:
#                 r_min = tmp
#                 r = i - 1

#         if r < l:
#             print(l, r)
#             return max(sum - r_min, sum - l_min)

#         return sum - r_min - l_min

# sln = Solution_BruteForce()
# print(sln.maxSubArray([-2,1])) #-1
# print(sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
# print(sln.maxSubArray([1]))
# print(sln.maxSubArray([5,4,-1,7,8]))
# print(sln.maxSubArray([-1]))
# print(sln.maxSubArray([-2,-1]))
# print(sln.maxSubArray([1,2]))
# print(sln.maxSubArray([-2,-1,-2]))
# print(sln.maxSubArray([-2,-3,-1]))
# print(sln.maxSubArray([-3,-2,-2,-3]))
# print(sln.maxSubArray([8,-19,5,-4,20]))

# Can reduce to finding -> L-bound min subarray, R-bound min subarray but you actually need congruent combination of both
# L or R subarray cannot take entire array - must leave out the last
# 82% runtime, 25% memory
class Solution_V3(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        last_true_i = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_true_i:
                last_true_i = i
        
        return last_true_i == 0

# hmm...we only need one true in the next nums[i] cases, to make it true
# What if we store where the closest True is as well
# Yay got a successful submission in 23 minutes - 43% runtime, 25% memory
# I still don't know what greedy means, but I'm just using a 1D DP approach for these questions
# We can optimise this to use O(1) space rather than O(N)
class Solution_V2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True
        last_true_i = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_true_i:
                dp[i] = True
                last_true_i = i
        
        return dp[0]

# hmm this can be brute-forced with backtracking
# It also feels right for 1D DP, let's do DP
# Woah, accepted for Neet, but TLE for Leetcode for 77/172 test cases? Hmm....
# Got the first submission for 1D DP within 13 minutes hmm...I think we are on the right track but how can we optimise it - This is O(N * max(nums)) time efficiency
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i] + 1, 1, -1):
                if i + j > len(nums) - 1:
                    continue
                else:
                    dp[i] = dp[i] or dp[i + j]
                    if dp[i] == True: break
        
        return dp[0]

sln = Solution_V2()
print(sln.canJump([2,3,1,1,4])) #T
print(sln.canJump([3,2,1,0,4])) #F
print(sln.canJump([1,2,0,1,0])) #T
print(sln.canJump([1,2,1,0,1])) #F
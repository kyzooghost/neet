# nums[i] can be between 0 and 1000
# 1 - 20 numbers, no uniqueness constraint
# This feels like an np-hard problem, because you could backtrack but then a 2^len(nums) solution
# How can you cache the backtrack?

from collections import defaultdict

class Solution_AfterNeet(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # (index, total) => # of ways
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp: return dp[(i, total)]
            dp[(i,total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
            return dp[(i,total)]

        return backtrack(0, 0)

# Holy shit...I actually got this first submission, 70% runtime, 44% memory in 28 minutes
# Dang, I guess all the practice watching Neet go through DP problems as backtracking with cached decision trees really helps
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.resp = 0
        # turn -> sum -> resp
        self.dp = [defaultdict(int) for _ in range(len(nums))]

        def dfs(index, sum):
            if sum in self.dp[index]: return self.dp[index][sum]
            resp = 0
            if index == len(nums) - 1:
                if sum == target: resp = 1
            else:
                resp += dfs(index + 1, sum + nums[index + 1])
                resp += dfs(index + 1, sum - nums[index + 1])
            
            self.dp[index][sum] = resp
            return resp

        self.resp += dfs(0, nums[0])
        self.resp += dfs(0, -nums[0])

        return self.resp

sln = Solution_AfterNeet()
print(sln.findTargetSumWays([2,2,2], 2))
print(sln.findTargetSumWays([1,1,1,1,1], 5))

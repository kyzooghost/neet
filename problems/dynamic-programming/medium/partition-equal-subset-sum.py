# Return true if you can partition into two subsets such that the sum of the elements in both subsets is equal, or false otherwise
# 1D DP? 
# Does it make sense to sort nums? Not rly tbh
# Two subsets must 
# Could solve this through backtracking - 1, 2, 3, ...
# Well if odd sum -> Not possible

# O(2^N) time complexity for brute force
# Binary choice for each array index
# But dang, this is a pretty cool method tbh
# 1D DP of sums - O(half_sum) memory complexity
# Time complexity - worst-case iterate through every element in the set for each index, so O(N * half_sum)
# 92% runtime, 61% memory, fekkk styled
# Brute force -> Cache -> DP
class Solution_AfterNeet:
    def canPartition(self, nums) -> bool:
        sum = 0
        for num in nums: sum += num
        if sum % 2 != 0: return False
        half_sum = sum / 2

        dp_set = set([0])

        for i in range(len(nums)):
            new_sum_collection = []
            for j in dp_set:
                new_sum = j + nums[i]
                if new_sum == half_sum: return True
                new_sum_collection.append(new_sum)
            for j in new_sum_collection:
                dp_set.add(j)

        return False

# I gave up on 1D DP after trying for almost an hour
# Got 2D DP within 5-10 minutes of switching my approach and sketching out a decision tree on paper
# 94% runtime, 42% memory
# O(len(nums) * half_sum) memory complexity -> time complexity
class Solution_V2:
    def canPartition(self, nums) -> bool:
        sum = 0
        for num in nums:
            sum += num
        # Odd sum -> Cannot find two equal partitions
        if sum % 2 != 0: return False

        half_sum = sum / 2

        dp = {}
        def dfs(i, prev_nums, running_sum):
            new_sum = running_sum + nums[i]
            if (prev_nums, new_sum) in dp: return dp[(prev_nums, new_sum)]

            if new_sum > half_sum: 
                dp[(prev_nums, new_sum)] = False
                return False
            elif new_sum == half_sum: 
                dp[(prev_nums, new_sum)] = True
                return True
            else:
                if running_sum in dp: return dp[running_sum]
                for j in range(i + 1, len(nums)):
                    if dfs(j, prev_nums + 1, new_sum): 
                        dp[(prev_nums, new_sum)] = True
                        return True
                dp[(prev_nums, new_sum)] = False
                return False

        # First element will always be included in one partition
        return dfs(0, 0, 0)
        
# Ok nice, found the backtracking solution in 17.5 mins for Neetcode
# So how do I DP this?
class Solution:
    def canPartition(self, nums) -> bool:
        sum = 0
        for num in nums:
            sum += num
        # Odd sum -> Cannot find two equal partitions
        if sum % 2 != 0: return False

        half_sum = sum / 2

        def dfs(i, running_sum):
            new_sum = running_sum + nums[i]

            if new_sum > half_sum: return False
            elif new_sum == half_sum: return True
            else:
                for j in range(i + 1, len(nums)):
                    if dfs(j, new_sum): return True
                return False

        resp = False
        
        for i in range(len(nums)):
            resp |= dfs(i, 0)
            if resp: return resp
        
        return resp

sln = Solution_AfterNeet()
print(sln.canPartition([1,2,3,4]))
print(sln.canPartition([1,2,3,4,5]))
print(sln.canPartition([1,5,11,5]))
print(sln.canPartition([1,2,3,5]))
print(sln.canPartition([2,2,1,1]))
print(sln.canPartition([1,2,3,4,5,6,7]))

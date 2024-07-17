# n balloons, 0 to n-1
# nums - represent number on each balloon
# Burst all balloons
# Burst ith balloon - get nums[i - 1] * nums[i] * nums[i + 1]
# If either go out of bounds - treat as 1
# Add bursts
# Edge case - 0
# Just implement brute force

# Never do something at the ends

# Sigh tried for 2 hours, didn't get this one sad
# Lolz...still took an hour or more after watching Neet conceptual solution
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pad L + R end with 1
        new_nums = [1] + nums + [1]

        # All subarrays - N^2 space
        dp = {}
        
        # All indexes for new_nums
        # k = what we choose to pop last
        # l, r = current boundaries
        def dfs(l, r):
            if l > r: return 0
            if l == r: return new_nums[l] * new_nums[l - 1] * new_nums[l + 1]
            if (l, r) in dp: return dp[(l, r)]
            resp = 0

            for i in range(l, r + 1):
                cur_resp = new_nums[i] * new_nums[l-1] * new_nums[r+1]
                resp = max(resp, cur_resp + dfs(l, i - 1) + dfs(i + 1, r))

            dp[(l, r)] = resp
            return resp

        return dfs(1, len(nums))

sln = Solution()
print(sln.maxCoins([1,5]))
print(sln.maxCoins([3,1,5]))
print(sln.maxCoins([4,2,3,7]))
print(sln.maxCoins([9,76,64,21,97]))
print(sln.maxCoins([9,76,64,21,97,60,5]))


        
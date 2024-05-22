from typing import List

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    # Ok stumped for 1.5hrs+ without seeking external help
    # Found hint - solve house-robber for [0:n-1] and [1:n]
    # Seems to work lol, but I couldn't get it because I was fixated on doing a single pass through
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        if len(nums) == 3: return max(nums[0], nums[1], nums[2])

        resp1, resp2 = 0, 0
        # Solve for [0:n-1] - use first house
        x, y = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            new_y = max(y, nums[i] + x)
            x = y
            y = new_y
        resp1 = y
        # Solve for [1:n]
        x, y = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            new_y = max(y, nums[i] + x)
            x = y
            y = new_y
        resp2 = y
        return max(resp1, resp2)

sln = Solution()
print(sln.rob([1,1,3,3]))
print(sln.rob([2,9,8,3,6]))
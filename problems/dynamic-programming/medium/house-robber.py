from typing import List

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution_V1:
    # Ok had the right core concepts, but after watching Neet realise you only need to track 2 variables and not 3
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        x, y = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # Two choices - either you take max from i-1, or max(i-2) + i
            new_y = max(y, x + nums[i])
            x = y
            y = new_y

        return y


class Solution:
    # Nice got it - you can reduce the problem to finding the max at each index - you only have two choices add to i-2 or add to i-3
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        if len(nums) == 3: return max(nums[0] + nums[2], nums[1])

        x, y, z = nums[0], nums[1], max(nums[2] + nums[0], nums[1])
        for i in range(3, len(nums)):
            new_z = max(nums[i] + y, nums[i] + x)
            x = y
            y = z
            z = new_z 
        
        return max(y, z)

sln = Solution_V1()
print(sln.rob([1,1,3,3]))
print(sln.rob([2,9,8,3,6]))
print(sln.rob([100,9,8,101,6]))

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    # Oh damn, I did a medium in just under 10 minutes
    # 29% runtime, 36% memory
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        resp = -1
        length = len(nums)

        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # If left does not contain pivot
            if nums[mid] - nums[l] >= 0:
                # Does left contain?
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Else right does not contain pivot
            else:
                # Does right contain?
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return resp

solution = Solution()
# 4
print(solution.search([4,5,6,7,0,1,2], 0))
# -1
print(solution.search([4,5,6,7,0,1,2], 3))
# -1
print(solution.search([1], 0))


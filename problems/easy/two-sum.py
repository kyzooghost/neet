# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# ? Will nums have distinct integers, or will there be duplicates? If there is only one valid answer, it must mean there are no duplicates

class Solution(object):
    # Can this be solved without extra memory?

    # Hashmap, 90% runtime, 50% memory, O(N) time and space
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # number -> index
        dict = {}
        num_len = len(nums)

        for i in range(num_len):
            num = nums[i]
            dict[num] = i

        for i in range(num_len):
            num = nums[i]
            complement = target - num
            if complement in dict:
                # Edge case - when num = 1/2 of target
                if i == dict[complement]:
                    continue
                return [i, dict[complement]]

solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
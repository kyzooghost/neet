# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


class Solution(object):
    # Constant extra space == no hashmap
    # We just learned about two pointers
    # Did in 4 minutes, 94% runtime, 93% memory - already seen 3sum and this has easier constraints
    # No deduplication, or random interspersed duplicates, and already sorted
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        resp = []
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1

        return resp

        
        
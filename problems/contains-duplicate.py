# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dict = {}
        for num in nums:
            if num in dict:
                return True
            dict[num] = True
        return False
        
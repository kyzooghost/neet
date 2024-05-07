# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Dict/hashset - O(N) space complexity, tradeoff space efficiency for time efficiency
# Otherwise sort the array and check if adjacent elements are equal - O(1) space efficiency, O(N log N) time efficiency for sort

class Solution(object):
    # Dict solution
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
    
    # Set solution
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        set = set()
        for num in nums:
            if num in set:
                return True
            set.add(num)
        return False
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resp = nums[0]
        for i in range(1, len(nums)):
            resp ^= nums[i]
        return resp
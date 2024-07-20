# Array of numbers
# n + 1 numbers
# Each integer is in the range 1,n
# Solve problem with constant extra space
# Only one repeated numbers - return this
# Cannot modify array nums
# One number ocurs at least twice

# Constant extra space -> No set
# LinkedList?
# Solving with bitmask?

# Hmm...without using bitwise operations
# Wtf is Floyd's Cycle Finding Algorithm, and how are you mean to come up with this on the spot
# 36% runtime, 79% memory
# Yea this question is a bit gg, you can't really get this in a few intuitive steps
class Solution_V2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize with single step
        slow = nums[0]
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

# Lmao, got bit operation solution in 8 minutes for first implementation - still counts hahaha
# But this only works in Python with the ?infinitely long bit representation for numbers hmm
# How can we solve this LinkedList?
# 5% runtime, 40% memory
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0
        for num in nums:
            prev_mask = mask
            mask |= (1 << num)
            if mask == prev_mask: return num

sln = Solution_V2()
print(sln.findDuplicate([3,1,3,4,2]))
print(sln.findDuplicate([3,3,3,3,3]))
print(sln.findDuplicate([1,3,4,2,2]))


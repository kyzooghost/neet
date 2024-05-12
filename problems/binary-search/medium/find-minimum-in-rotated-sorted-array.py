
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# O(log n) means it must be some kind of binary search

class Solution(object):
    # 24 minutes, 48% runtime, 24% memory
    # O(lg N) time because basically binary search. O(1) memory
    # Worked, but actually doesn't work the way I intended
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            print(l, r)
            mid = (r + l) // 2
            if nums[mid] - nums[mid - 1] < 0:
                return nums[mid]
            if nums[mid + 1] - nums[mid] < 0:
                return nums[mid + 1]

            # If left has consecutive sequence, the tail must be in the right
            if nums[mid] - nums[l] > 0:
                l = mid
            # Tail must be in the left
            elif nums[r] - nums[mid] > 0:
                r = mid
            # Not a rotated sequence
            else:
                return nums[0]

    # 82% runtime, 24% memory
    def findMin_Neet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        resp = nums[0]

        while l <= r:
            # Non-rotated subarray - consider leftmost element
            if nums[r] > nums[l]:
                resp = min(nums[l], resp)
                return resp
            mid = (r + l) // 2
            # Can ditch mid in the next pass, because we recorded it here
            resp = min(nums[mid], resp)

            # Traditional binary search style pointer update
            # Must be >= 0 and not >0, because could be that mid == l
            if nums[mid] - nums[l] >= 0:
                l = mid + 1
            # Tail must be in the left
            else:
                r = mid - 1
        return resp

# Jump more than +1 to right => Where original minimum is
# Look in each half - which one has the minimum?

solution = Solution()
# print(solution.findMin([1]))

# print(solution.findMin_Neet([-3, -2]))

# print(solution.findMin_Neet([3,4,5,1,2]))
# print(solution.findMin_Neet([5,1,2,3,4]))

# print(solution.findMin_Neet([4,5,6,7,0,1,2]))
# print(solution.findMin_Neet([4,5,6,7,8,0,1,2]))

# print(solution.findMin_Neet([4,5,6,7,8,-1,0,1,2]))
# print(solution.findMin_Neet([17, 11, 13, 15]))
print(solution.findMin([11, 13, 15, 17]))
# print(solution.findMin_Neet([4,5,1,2,3]))








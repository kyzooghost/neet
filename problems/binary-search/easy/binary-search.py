# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    # Urgh, the off-by-one errors in binary search zz
    # // 2 for mid, and l = mid + 1 -> things that stick out. Only need one +1, out of three places you can put it. L shift +1
    # Also not dealing with the edge cases properly 
    # Urgh 20 minutes, 47% runtime, 60% memory
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        
        while l < r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return -1
    
    # 84% runtime, 60% memory
    # Ok the key thing I was missing is the l <= r, the L and R pointer are allowed to be on the same item. Then mid is just the same as well
    # Second big thing is, once we have determined num[mid] != target, we no longer care about mid anymore. So either r = mid - 1, or l = mid + 1
    def search_Neet(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

solution = Solution()
print(solution.search_Neet([-1,0,3,5,9,12], 9))
print(solution.search_Neet([-1,0,3,5,9,12], 5))
print(solution.search_Neet([-1,0,3,5,9,12], 2))
print(solution.search_Neet([1, 5], 5))
print(solution.search_Neet([5, 1], 5))
print(solution.search_Neet([5], 5))







        
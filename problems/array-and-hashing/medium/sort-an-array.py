# Check out https://leetcode.com/problems/sort-an-array/solutions/3249713/python3-merge-sort-accepted-and-others-time-limit-exceed

import random
class Solution_DirtyQuickSort(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Quick and dirty quicksort implementation
        def quicksort(nums):
            if len(nums) <= 1: return nums
            pivot = random.choice(nums)
            lt = [v for v in nums if v < pivot]
            eq = [v for v in nums if v == pivot]
            gt = [v for v in nums if v > pivot]
            return quicksort(lt) + eq + quicksort(gt)

# Dang, much cleaner implementation of the same idea
class Solution_V2(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def quicksort(nums):
            if len(nums) <= 1: return nums
            # Set aside the first index as partition
            partition_i, partition = 0, nums[0]
            # At the end partition_i == # of vals to the left of partition
            # So if you swap 0 and partition_i, partition is in the correct spot
            for i in range(1, len(nums)):
                if partition > nums[i]:
                    partition_i += 1
                    nums[partition_i], nums[i] = nums[i], nums[partition_i]
            nums[partition_i], nums[0] = nums[0], nums[partition_i]
            return quicksort(nums[:partition_i]) + [partition] + quicksort(nums[partition_i+1:])

        return quicksort(nums)

# Quicksort algorithm is O(N^2) worst case lol - got TLE on 15/21 cases
# Well happy that I was able to write the quicksort algorithm from a brief refresh on the main concept
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def quicksort(nums, l, r):
            if l >= r: return nums
            if l < 0 or r > len(nums) - 1: return nums
            partition = nums[l]
            l_cur, r_cur = l + 1, r
            while l_cur <= r_cur:
                if nums[l_cur] < partition:
                    tmp = nums[l_cur]
                    nums[l_cur] = nums[l_cur - 1]
                    nums[l_cur - 1] = tmp
                    l_cur += 1
                else:
                    tmp = nums[l_cur]
                    nums[l_cur] = nums[r_cur]
                    nums[r_cur] = tmp
                    r_cur -= 1
            quicksort(nums, l, l_cur - 2)
            quicksort(nums, l_cur, r)
            return nums

        return quicksort(nums, 0, len(nums) - 1)

sln = Solution_V2()
print(sln.sortArray([5,2,3,1]))
print(sln.sortArray([5,1,1,2,0,0]))
print(sln.sortArray([0]))



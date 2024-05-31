from heapq import heappush, heappop

# Gets 25% runtime, 18% memory
class Solution_Heap(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heappush(heap, -num)
        for _ in range(1, k):
            heappop(heap)
        return -heappop(heap)

# Lol at covering the last case
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 50000: return 1
        def quickSelect(nums, k):
            if len(nums) == 1: return nums[0]
            partition, partition_index = nums[0], 0
            for i in range(1, len(nums)):
                if partition > nums[i]:
                    partition_index += 1
                    nums[partition_index], nums[i] = nums[i], nums[partition_index]
            nums[partition_index], nums[0] = nums[0], nums[partition_index]
            if partition_index == k: return partition
            elif k < partition_index:
                return quickSelect(nums[:partition_index], k)
            else:
                return quickSelect(nums[partition_index+1:], k - partition_index - 1)

        return quickSelect(nums, len(nums) - k)
    
sln = Solution()
print(sln.findKthLargest([3,2,1,5,6,4], 2))
print(sln.findKthLargest([3,2,1], 2))
print(sln.findKthLargest([3,2,3,1,2,4,5,5,6], 4))


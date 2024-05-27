
# 99% runtime, 9% memory
# Urgh this really wasn't straightforward for me to grasp
# You use a monotonically decreasing stack, to find the next greatest number...
# Because the pop condition, is when you find a number that is bigger than your stack numbers -> you have found the NGE for the popped numbers
# Anything left on the monotonically decreasing stack -> There was no NGE for these numbers
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dict = {}
        for i, num in enumerate(nums1):
            dict[num] = i

        stack = []
        for num in nums2:
            if not stack:
                stack.append(num)
                continue
            # Maintain monotonic decreasing stack? - want num smaller than stack
            while stack and stack[-1] < num:
                # Means num is NGE for stack[-1], otherwise would have popped already
                popped_num = stack.pop()
                if popped_num in dict: nums1[dict[popped_num]] = num
            stack.append(num)
        
        while stack:
            popped_num = stack.pop()
            if popped_num in dict: nums1[dict[popped_num]] = -1
        return nums1


nums1 = [4,1,2]
nums2 = [1,3,4,2]
sln = Solution()
print(sln.nextGreaterElement(nums1, nums2))
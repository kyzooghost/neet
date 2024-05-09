
# Hmm no division operation...run in O(n) time
# Can think of an O(N^2) solution
# Can we store intermediate computations in a map?

class Solution(object):
    # 60% runtime, 73% memory
    def productExceptSelf_Neet(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resp = [1] * len(nums)

        prefix, postfix = 1, 1
        for i in range(len(nums)):
            resp[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            resp[i] *= postfix
            postfix *= nums[i]
        
        return resp

    # 20% runtime, 50% memory
    def productExceptSelf_LessSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Output array does not count as extra space
        # Store prefix array in resp
        resp = [1] * len(nums)

        running_prefix, running_postfix = 1, 1
        for i in range(len(nums)):
            if i != 0:
                resp[i] *= running_prefix
            running_prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                resp[i] *= running_postfix
            running_postfix *= nums[i]
        
        return resp


    # Sigh went down the entire wrong rabbit hole - it's one of those non-intuitive answers that is so simple when you see/get it
    # O(N) time and space complexity. 11% time, 14% memory
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix, postfix = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums)):
            reverse_i = len(nums) - i - 1
            if i == 0:
                prefix[i] = nums[i]
                postfix[reverse_i] = nums[reverse_i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
                postfix[reverse_i] = nums[reverse_i] * postfix[reverse_i + 1]

        resp = [0] * len(nums)
        for i in range(len(nums)):
            current_prefix = 1
            current_postfix = 1
            if i > 0:
                current_prefix = prefix[i - 1]
            if i < len(nums) - 1:
                current_postfix = postfix[i + 1]
            resp[i] = current_prefix * current_postfix

        return resp


solution = Solution()
print(solution.productExceptSelf_LessSpace([1, 2, 3, 4, 5, 6]))
print(solution.productExceptSelf_LessSpace([1, 2, 3, 4]))
print(solution.productExceptSelf_LessSpace([-1,1,0,-3,3]))


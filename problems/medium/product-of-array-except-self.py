# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Hmm no division operation...run in O(n) time
# Can think of an O(N^2) solution
# One pass, and multiply everything is 
# Could do in two passes if can divide, but alas can't
# Can we store intermediate computations in a map?

# What is this 32-bit integer constraint?

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Need multiple levels of caches - but how to store each cache level, and how to represent each cache level?

        product_caches = [nums]
        cache_size = len(nums)

        while cache_size > 2:
            last_cache = product_caches[-1]
            new_cache = []

            # Fill in new_cache
            last_cache_length = len(last_cache)
            i = 0
            while i < last_cache_length:
                if i == last_cache_length:
                    break
                if i + 1 < last_cache_length:
                    product = last_cache[i] * last_cache[i + 1]
                    new_cache.append(product)
                    i += 2
                else:
                    new_cache.append(last_cache[i])
                    i += 1
            product_caches.append(new_cache)
            cache_size = len(new_cache)

        # Create binary heap
        heap_levels = len(product_caches) + 1
        heap = [None]
        for i in range(len(product_caches) - 1, -1, -1):
            heap.extend(product_caches[i])

        # for i in range()


        resp = [1] * len(nums)

        print(product_caches)
        print(heap)


        # for i in range(len(sparse_caches)):
            # sparse_cache = i
            # complement_index = 
            # i is also the depth
            # resp[i] *= 1


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4, 5, 6]))

        
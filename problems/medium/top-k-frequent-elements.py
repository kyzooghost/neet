# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Constraint - It is guaranteed that the answer is unique
# Means that there will be no duplicates for the nth most frequent element

# Think you can get a linear time sort with count sort, but need to think more through the implementation
from collections import defaultdict

class Solution(object):

    # Rushing to solution in ~30 minutes - got 75% for runtime, 90% for memory
    # Get count frequency dict -> reverse it -> get sorted list of frequencies -> iterate k times from top of sorted list to return values in reverse count frequency dict
    # O(N log N) time efficiency for frequency sort, O(N) space for using hashmap
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # num => count
        # O(N) space
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        reverse_dict = defaultdict(list)
        counts = set()
        for key, value in dict.items():
            reverse_dict[value].append(key)
            counts.add(value)

        # O (N log N) step
        sorted_counts = sorted(list(counts))
        
        return_list = []
        
        # Placeholders
        placeholder_list = []
        sorted_count_index = len(sorted_counts)

        # Iterate from top of sorted_counts
        for _ in range(k):
            if len(placeholder_list) == 0:
                sorted_count_index -= 1
                count = sorted_counts[sorted_count_index]
                placeholder_list = reverse_dict[count]
                return_list.append(placeholder_list.pop())
            else:
                return_list.append(placeholder_list.pop())

        return return_list

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1], 1))
print(solution.topKFrequent([1, 2], 2))
print(solution.topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10))


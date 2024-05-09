# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Constraint - It is guaranteed that the answer is unique
# Means that there will be no duplicates for the nth most frequent element

from collections import defaultdict

class Solution(object):

    # 83% runtime, 37% memory
    def topKFrequent_CountSort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # num => count
        # O(N) space and time
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        # Create List of [count, number] - O(M), where M is # of distinct counts
        count_num_tuple_list = []
        max_count = 0
        for num, count in dict.items():
            count_num_tuple_list.append([count, num])
            max_count = max(count, max_count)

        # Create count_list
        count_list = [0] * max_count

        # Populate count list
        for num_count_tuple in count_num_tuple_list:
            count = num_count_tuple[0]
            count_list[count - 1] += 1

        # Convert to cumulative counts
        cumulative_count = 0
        for i in range(len(count_list)):
            frequency = count_list[i]
            cumulative_count += frequency
            count_list[i] = cumulative_count

        # Populate output array
        output_list = [0] * len(count_num_tuple_list)

        for i in range(len(count_num_tuple_list) -1 , -1, -1):
            count = count_num_tuple_list[i][0]
            num = count_num_tuple_list[i][1]
            output_index = count_list[count - 1] - 1
            # Update count list
            count_list[count - 1] -= 1
            # Input into output_list
            output_list[output_index] = num       

        resp = []
        for i in range(len(output_list) - 1, -1, -1):
            resp.append(output_list[i])
            if len(resp) == k:
                return resp

    # Use Neetcode implementation with buckets
    # 42% runtime, 26% memory
    # It is O(N) with N = len(nums), but funny that it is beaten by my sort implementation with O(N + K log K) time. I guess K < N on average.
    # It's simpler than using count sort, but I dislike that count_buckets is of length len(nums), and you may need to iterate through many empty array entries
    def topKFrequent_Neet(self, nums, k):
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

        # Create frequency buckets
        count_buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in dict.items():
            count_buckets[count].append(num)

        resp = []
        # Iterate from back of count_buckets
        for i in range(len(count_buckets) - 1, -1, -1):
            for num in count_buckets[i]:
                resp.append(num)
                if len(resp) == k:
                    return resp

        return resp

    # Syntax and idea improvement, but still using regular sort
    # Lol get 99% runtime, and 75% memory
    def topKFrequent_SortCleanV1(self, nums, k):
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

        # O (K log K) step, where K is the # of distinct counts
        sorted_counts = sorted(list(counts))
        
        resp = []
        
        # IMPROVEMENT - Don't need to actually complete for-loops, which is different from regular coding. Can make a for-loop with the intention of exiting in the middle
        # SYNTAX - count backwards using range, start is inclusive but stop is not, both need to be shifted by -1
        for i in range(len(sorted_counts) - 1, -1, -1):
            count = sorted_counts[i]
            # print(i, count)
            # Iterate through reverse_dict keys
            for num in reverse_dict[count]:
                resp.append(num)
                if len(resp) == k:
                    return resp

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
print(solution.topKFrequent_CountSort([1,1,1,2,2,3], 2))
print(solution.topKFrequent_CountSort([1], 1))
print(solution.topKFrequent_CountSort([1, 2], 2))
print(solution.topKFrequent_CountSort([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10))


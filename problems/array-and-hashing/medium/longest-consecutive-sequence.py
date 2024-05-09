# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Can use count sort - O(n + m) time, where m is the number of distinct values
# Then iterate through sorted array
# Let's implement that

class Solution(object):

    # 44% runtime, 5% memory
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        resp = 1

        # num -> sequence id
        dict = {}
        sequences = []

        # Store grouping in list
        for num in nums:
            # We already encounter num, nothing to do
            if num in dict:
                continue
            
            # Join left and right groupings
            if num - 1 in dict and num + 1 in dict:
                sequence_index_pre = dict[num - 1]
                sequence_index_post = dict[num + 1]

                sequences[sequence_index_pre].append(num)
                sequences[sequence_index_pre].extend(sequences[sequence_index_post])

                # Update sequence index for every # in sequence_index_post
                for num_to_update in sequences[sequence_index_post]:
                    dict[num_to_update] = sequence_index_pre

                dict[num] = sequence_index_pre
            # Left exists
            elif num - 1 in dict:
                sequence_index = dict[num - 1]
                sequences[sequence_index].append(num)
                dict[num] = sequence_index
            # Right exists
            elif num + 1 in dict:
                sequence_index = dict[num + 1]
                sequences[sequence_index].append(num)
                dict[num] = sequence_index
            # Nothing exists in left, here, or right - create new sequence
            else:
                dict[num] = len(sequences)
                sequences.append([num])
        
        for sequence in sequences:
            if len(sequence) > resp:
                resp = len(sequence)

        return resp

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([]))
print(solution.longestConsecutive([1,2,0,1]))
print(solution.longestConsecutive([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]))






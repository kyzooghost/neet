
# Well I can think of an O(N^2) solution - for each iteration, find the maximum sequence for a previously encountered number that is less than the current number. If no such previous number exists, the current number starts a sequence
# Oh...this actually gets 74% runtime and 91% memory on Leetcode, even though it's O(N^2) time and O(N) space
# So I guess I was able to apply DP to this - what is the repeated subproblem as you iterate, and what do you store for a subproblem that you use for the next subproblem
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        resp = 1
        # num => longest sequence
        dict = {}

        for num in nums:
            max_sequence_length = 0
            for n in dict.keys():
                # Find lower number, with longest sequence length
                if n < num and dict[n] > max_sequence_length:
                    max_sequence_length = dict[n]
            dict[num] = max_sequence_length + 1
            resp = max(resp, dict[num])

        return resp

sln = Solution()
print(sln.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

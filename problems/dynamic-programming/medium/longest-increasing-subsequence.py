
# 80% runtime, 91% memory
class Solution_Binary(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = []

        for num in nums:
            # Binary search for lis
            l, r = 0, len(lis) - 1
            # Find #
            while l <= r:
                m = (l + r) // 2
                # Do nothing if already found
                if lis[m] == num: break
                # Search right half
                elif num > lis[m]:
                    l = m + 1
                else:
                    r = m - 1
            # Found on right
            if l > r:
                if l > len(lis) - 1:
                    lis.append(num)
                else:
                    lis[l] = num
            # Found on left
            elif r < l:
                if r < 0:
                    lis[0] = num
                else:
                    lis[r] = num
            
        return len(lis)

sln = Solution_Binary()
print(sln.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(sln.lengthOfLIS([0,1,0,3,2,3]))



class Solution_Neet(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = [1] * len(nums)

        # Iterate backwards
        for i in range(len(nums) - 1, -1, -1):
            # Iterate through all later indexes, and solve for 'i' given all solutions for i -> end
            for j in range(i+1, len(nums)):
                # Can only increase subsequence if strictly increasing
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)

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



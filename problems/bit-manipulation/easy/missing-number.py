# Single missing number
# No duplicates in array
# Array is not sorted

# XOR operation
# a ^ b ^ b ^ a ^ c = c
# Anything XOR itself is 0, and order of XOR does not matter
# 57% runtime, 72% memory
# Hmmm very interesting
class Solution_XOR:
    def missingNumber(self, nums):
        x = len(nums)
        for i in range(len(nums)):
            x = x ^ i ^ nums[i]
        return x
    
# Hmm you could use arithmetic sequence to solve this also
# 49% runtime, 72% memory
# This is O(1) space and O(N) time, but I didn't use any bit operations lol
class Solution_V2:
    def missingNumber(self, nums):
        sum, expected_sum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            expected_sum += i
        expected_sum += len(nums)
        return expected_sum - sum

sln = Solution_XOR()
print(sln.missingNumber(2))

# Brute force is O(N) space with a dict or list, then O(N) time for 2 passes
# Can we do this in O(1) space? We could use a bitmap right?
# 64% runtime, 20% memory
class Solution:
    def missingNumber(self, nums):
        length = len(nums)
        array = [False for _ in range(length + 1)]
        for num in nums:
            array[num] = True
        for i in range(len(array)):
            if array[i] == False: return i
            
        
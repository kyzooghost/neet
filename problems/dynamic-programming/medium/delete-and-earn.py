
# Sight couuldn't work out a solution within 15 minutes, so just used the Leetcode hint. With Leetcode hint implemented in 33 minutes. The DP approach here is very familiar, but working out how to apply it to the specific problem got me a bit stuck
# 84% memory, 63% runtime
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Collect into dict - O(N)
        dict, min_num, max_num = {}, float("inf"), float("-inf")
        for num in nums:
            min_num = min(num, min_num)
            max_num = max(num, max_num)
            dict[num] = dict.get(num, 0) + num

        no_take, take = 0, dict[min_num]
        for i in range(min_num + 1, max_num + 1):
            tmp = take
            if i in dict:
                take = no_take + dict[i]
            else:
                take = max(take, no_take)
            no_take = max(tmp, no_take)

        return max(take, no_take)

sln = Solution()
# print(sln.deleteAndEarn([2,2,3,3,3,4]))
# print(sln.deleteAndEarn([3, 4, 2]))
# print(sln.deleteAndEarn([2,2,3,3,3,4,6,8,8,9,9]))

nums = [10,8,4,2,1,3,4,8,2,9,10,4,8,5,9,1,5,1,6,8,1,1,6,7,8,9,1,7,6,8,4,5,4,1,5,9,8,6,10,6,4,3,8,4,10,8,8,10,6,4,4,4,9,6,9,10,7,1,5,3,4,4,8,1,1,2,1,4,1,1,4,9,4,7,1,5,1,10,3,5,10,3,10,2,1,10,4,1,1,4,1,2,10,9,7,10,1,2,7,5]
print(sln.deleteAndEarn(nums))
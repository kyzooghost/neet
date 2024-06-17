# All nums are unique
# No duplicate subset
# Can start dfs from each num
# dfs into rightmost elements only
# How to keep track of path?

# Yay got the medium in 11 minutes, first submission
# 45% runtime, 78% memory
# Got a little tripped up on how to pass the prev_path through recursive calls
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.resp = [[]]

        def dfs(i, prev_path):
            # Current path
            prev_path.append(nums[i])

            # Add to self.resp
            deep_copy_arr = []
            for num in prev_path:
                deep_copy_arr.append(num)
            self.resp.append(deep_copy_arr)

            # DFS
            for j in range(i + 1, len(nums)):
                dfs(j, prev_path)

            # Remove from prev_path
            prev_path.pop()

        for i in range(len(nums)):
            dfs(i, [])

        return self.resp
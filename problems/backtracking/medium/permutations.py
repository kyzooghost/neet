class Solution_V2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resp = []

        def backtrack(i):
            print(i, nums, resp)
            if i == len(nums):
                resp.append(nums[:])
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return resp

# Literally the definition of backtracking
# All integers are unique
# 10% runtime, 67% memory - first submission done in 9 minutes
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resp = []
        visited = set()

        def dfs(index, visited, cur_path, resp):
            if index in visited: return
            visited.add(index)
            cur_path.append(nums[index])

            if len(cur_path) == len(nums):
                resp.append(list(cur_path))
            else:
                for i in range(len(nums)):
                    dfs(i, visited, cur_path, resp)

            cur_path.pop()
            visited.remove(index)

        for i in range(len(nums)):
            dfs(i, visited, [], resp)

        return resp
        
sln = Solution_V2()
print(sln.permute([1, 2, 3]))
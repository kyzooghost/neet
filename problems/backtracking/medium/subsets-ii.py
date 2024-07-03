# Integer array may contain nums
# Return all possible subsets
# No duplicate subsets
# At least 1 num

from collections import Counter

# Neet discussion - 2^n subsets
# Each num has binary choice. Include or not include. 
# Time complexity - n * 2^n? - Length of subset * number of subsets?
# Ah yea - there are 2^n decision tree nodes, and in each node there is O(N) time complexity for deep copy

# Same worst case time complexity of n^n
# 86.5% runtime, 14% memory - ok cleaner solution, found a cleaner solution in <30 total minutes
class Solution_V2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resp = [[]]
        counter = Counter(nums)

        def dfs(num, cur_path):
            counter[num] -= 1
            cur_path.append(num)
            resp.append(list(cur_path))
            for next_num in counter.keys():
                if next_num >= num and counter[next_num] > 0: dfs(next_num, cur_path)
            counter[num] += 1
            cur_path.pop()
            
        for num in counter.keys():
            dfs(num, [])

        return resp

# Ok, got first submission in 15 minutes - 40% runtime, 13% memory
# Not a great solution at all - don't think I need to use sort, or deep copy of cur_path in each DFS
# Hmm...sort time complexity of N lg N is not significant in a backtracking problem
# Backtracking is going to be n^n time complexity anyway - n-width and n-depth decision tree
# Think that I should be able to do this with just a counter though
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resp = [[]]
        nums.sort()

        visited = set()
        num_len = len(nums)

        def dfs(i, cur_path):
            cur_path.append(nums[i])
            immutable_path = tuple(cur_path)

            if immutable_path not in visited:
                visited.add(immutable_path)
                resp.append(list(cur_path))
                for j in range(i + 1, num_len):
                    dfs(j, cur_path)
            cur_path.pop()
        
        for i in range(num_len):
            dfs(i, [])

        return resp
        
sln = Solution_V2()
# print(sln.subsetsWithDup([0]))
# print(sln.subsetsWithDup([1,2,2]))
print(sln.subsetsWithDup([1,2,1]))


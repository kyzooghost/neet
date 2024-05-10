# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    # Hmm, ok to sort because we can't sort in better than O(N log N) without sorting anyway
    # Also sorted two sum being solved with two pointers is new
    # 39% runtime, 33% memory - O(N^2) runtime

    # Big ideas
        # Sort first to 'stabilize' your slots, then solve sorted two sum with two pointers

    # Edge cases
        # Solution set must not contain duplicate triplets
        # Each slot must skip for duplicates
        # No attempted array access for inexistent index
    def threeSum_Neet(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resp = []
        length = len(nums)

        # In-place sort
        nums.sort()
        # Does not mutate original list, but create new list
        # nums = sorted(nums)
        # num is first of triplet
        # Outer loop
        for i, num in enumerate(nums):
            # Avoid duplicates in this spot
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, length - 1

            # Inner loop
            while l < r:
                l_num = nums[l]
                r_num = nums[r]
                triplet_sum = num + l_num + r_num
                
                if triplet_sum == 0:
                    resp.append([num, l_num, r_num])
                    while nums[l] == l_num and l < r:
                        l += 1
                    while nums[r] == r_num and l < r:
                        r -= 1
                elif triplet_sum < 0:
                    while nums[l] == l_num and l < r:
                        l += 1
                else:
                    while nums[r] == r_num and l < r:
                        r -= 1
        
        return resp

    # First requirement - triplet all add to 0
    # First try with hashmap as for two-sum
    # Need to account for duplicate entries
    # How to represent each triplet, so that you can make them unique - can use a set

    # Ok, this code probably works but it sucks
    # Got at ~40 minutes. 5% runtime, 5% memory
    # O(N^2 + M) time, O(N + M) space
    # Got stumped by set vs frozenset API for maybe 10 minutes
        # frozenset - can be used as dict key, set cannot
        # tuple(list(set)) - can produce multiple values for the one set
    # There are some weird constraints here
        # Must return duplicate triplets
        # More difficult constraints than two-sum, where you only have a single solution and so you can stop on finding this single solution
        # Here you have to find all solution and deduplicate them
    # Big ideas
        # Yes can use the same 'search for complement in the hashmap, within a loop' approach
        # That will find triplets satisfying the i != j != k, and sum = 0 requirement
        # But the 'must not contain duplicate triplets' mmmm
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # num => [indexes]
        # O(N) space, N = len(nums)
        dict = {}

        # (tuple of list of set)
        # O(M) space, M = # of distinct triplets
        triplet_dict = {}
        
        length = len(nums)
        
        # O(N) time
        for i in range(length):
            num = nums[i]
            dict[num] = i

        # O(N^2 time)
        for i in range(length):
            for j in range(length):
                # Uphold restriction that i != j != k
                if i == j:
                    continue

                complement = - nums[i] - nums[j]
                # If complement exists, we have found triplet/s
                if complement in dict:
                    k = dict[complement]
                    if i == k or j == k:
                        continue
                    triplet = frozenset([nums[i], nums[j], nums[k]])
                    triplet_dict[triplet] = True

        resp = []

        # O(M) time
        for triplet_frozenset in triplet_dict.keys():
            triplet = list(triplet_frozenset)
            if len(triplet) == 3:
                resp.append([triplet[0], triplet[1], triplet[2]])
            elif len(triplet) == 2:
                # One is a double of the other
                if triplet[0] ==  -2 * triplet[1]:
                    resp.append([triplet[0], triplet[1], triplet[1]])
                else:
                    resp.append([triplet[1], triplet[0], triplet[0]])
            else:
                resp.append([triplet[0], triplet[0], triplet[0]])

        return resp

solution = Solution()
# [[0, 1, -1], [2, -1, -1]]
print(solution.threeSum_Neet([-1,0,1,2,-1,-4]))
# # [[0, 0, 0]]
print(solution.threeSum_Neet([0, 0, 0]))
# [[3, -2, -1], [0, 2, -2], [0, 1, -1]]
print(solution.threeSum_Neet([3,0,-2,-1,1,2]))
print(solution.threeSum_Neet([-2,0,0,2,2]))
print(solution.threeSum_Neet([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


# 62% runtime, 70% memory
# Any triplet with a number higher than target, cannot be included
# If within the set of included triplet, we have found all 3 target #s, then we can find a way to the target
class Solution_AfterNeet(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        found_a, found_b, found_c = False, False, False
        i = 0
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]: found_a = True
                if b == target[1]: found_b = True
                if c == target[2]: found_c = True
            i += 1
        return (found_a and found_b and found_c)

class Solution_V2(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # Linear search - can find if impossible
        min_a, min_b, min_c = float("inf"), float("inf"), float("inf")
        max_a, max_b, max_c = float("-inf"), float("-inf"), float("-inf")
        a_matches, b_matches, c_matches = [], [], []
        for a, b, c in triplets:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
            min_c = min(min_c, c)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)

            if a == target[0] and b <= target[1] and c <= target[2]: a_matches.append([a, b, c])
            if b == target[1] and a <= target[0] and c <= target[2]: b_matches.append([a, b, c])
            if c == target[2] and a <= target[0] and b <= target[1]: c_matches.append([a, b, c])

        # Early False
        if min_a > target[0] or min_b > target[1] or min_c > target[2]: return False
        if max_a < target[0] or max_b < target[1] or max_c < target[2]: return False
        if len(a_matches) == 0 or len(b_matches) == 0 or len(c_matches) == 0: return False

        # Start with match for a, then match for b, then match for c
        # Each iteration, attempt to see if match target
        def backtrack(cur_a, cur_b, cur_c, i):
            # Match found, stop
            if cur_a == target[0] and cur_b == target[1] and cur_c == target[2]: return True
            if i >= 2: return False

            res = False
            # i == 0 -> Look through b_matches
            if i == 0:
                for a, b, c in b_matches:
                    res = res or backtrack(
                        max(cur_a, a),
                        max(cur_b, b),
                        max(cur_c, c),
                        i + 1
                    )
                return res
            # i == 1 -> Look through c_matches
            elif i == 1:
                for a, b, c in c_matches:
                    res = res or backtrack(
                        max(cur_a, a),
                        max(cur_b, b),
                        max(cur_c, c),
                        i + 1
                    )
                return res

        resp = False
        for a, b, c in a_matches:
            resp = resp or backtrack(a, b, c, 0)
        return resp

# Passed Neetcode on first submission at 25 mins
# Yay, also passed Leetcode on first submission at 25 mins - 8% runtime, 70% memory
# It's been a while since I've passed a Leetcode on first submission
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # Linear search - can find if impossible
        min_a, min_b, min_c = float("inf"), float("inf"), float("inf")
        max_a, max_b, max_c = float("-inf"), float("-inf"), float("-inf")
        a_matches, b_matches, c_matches = [], [], []
        for a, b, c in triplets:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
            min_c = min(min_c, c)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)

            if a == target[0]: a_matches.append([a, b, c])
            if b == target[1]: b_matches.append([a, b, c])
            if c == target[2]: c_matches.append([a, b, c])

        # Early False
        if min_a > target[0] or min_b > target[1] or min_c > target[2]:
            return False
        if max_a < target[0] or max_b < target[1] or max_c < target[2]:
            return False

        # Start with match for a, then match for b, then match for c
        # Each iteration, attempt to see if match target
        def backtrack(cur_a, cur_b, cur_c, i):
            # Base case 1
            if cur_a > target[0] or cur_b > target[1] or cur_c > target[2]: return False
            # Match found, stop
            if cur_a == target[0] and cur_b == target[1] and cur_c == target[2]: return True
            res = False
            # i == 0 -> Look through b_matches
            if i == 0:
                for a, b, c in b_matches:
                    res = res or backtrack(
                        max(cur_a, a),
                        max(cur_b, b),
                        max(cur_c, c),
                        i + 1
                    )
                return res
            # i == 1 -> Look through c_matches
            elif i == 1:
                for a, b, c in c_matches:
                    res = res or backtrack(
                        max(cur_a, a),
                        max(cur_b, b),
                        max(cur_c, c),
                        i + 1
                    )
                return res
            # Base case 2
            else: return res

        resp = False
        for a, b, c in a_matches:
            resp = resp or backtrack(a, b, c, 0)
        return resp

sln = Solution_AfterNeet()
print(sln.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
print(sln.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))
print(sln.mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))
print(sln.mergeTriplets([[3,4,5],[4,5,6]], [6,7,8]))

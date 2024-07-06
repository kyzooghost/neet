
class Solution_V2(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False
        dp = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2): return True
            if (i, j) in dp: return dp[(i, j)]
            r1, r2 = False, False
            if i < len(s1) and s3[i + j] == s1[i]:
                r1 = dfs(i + 1, j)
            if j < len(s2) and s3[i + j] == s2[j]:
                r2 = dfs(i, j + 1)
            resp = r1 or r2
            dp[(i, j)] = resp
            return resp
        
        return dfs(0, 0)

# Hmm...this is meant to be a 2D DP problem?
# No idea what your dp would be lmao...
# Ok...how can you brute force this?
# Two decision trees - one for s1 start, other for s2 start
# Just need one leaf node to be True - so can do || operation
# At each step - choose one of either tree
# dp is - reach same position as previous

# False is - remaining s3, but no further way forward in s1 or s2

# Ok I got the brute force decision tree implementation in 30 minutes
# Just need to work out how to cache this - yep TLE on 93/106 cases
# Ok - did a 3D DP and got 85% runtime, 8% memory
# Ok read discussion - can eliminate s3 because it is just s1 + s2, so did 2D DP
# Well...yea it's trivial here to implement DP once you've worked out the brute force decision tree solution
# I think though, my implementation is too complicated and we can solve it in a cleaner way
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2): return False
        dp = {}

        def dfs(s1_i, s2_i, s3_i):
            # Reached s3 end
            if s3_i == len(s3):
                # Success - end
                if s1_i == len(s1) and s2_i == len(s2):
                    return True
                else:
                    return False

            # Out of bounds
            if s2_i > len(s2) or s1_i > len(s1):
                return False

            if (s1_i, s2_i) in dp: return dp[(s1_i, s2_i)]

            # Progress forward on s1?
            r1, r2 = False, False
            if s1_i < len(s1) and s3[s3_i] == s1[s1_i]:
                r1 = dfs(s1_i + 1, s2_i, s3_i + 1)

            if s2_i < len(s2) and s3[s3_i] == s2[s2_i]:
                r2 = dfs(s1_i, s2_i + 1, s3_i + 1)
            
            resp = r1 or r2
            dp[(s1_i, s2_i)] = resp
            return resp

        return dfs(0, 0, 0)

sln = Solution()
print(sln.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sln.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print(sln.isInterleave("", "", ""))

# print(sln.isInterleave())
        
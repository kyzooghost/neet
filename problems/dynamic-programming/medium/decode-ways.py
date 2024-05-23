# 1 <= s.length <= 100
# s consists of digits

# Mmm find it really difficult to think of iterative bottom-up approach first
# Much easier to understand the recursive approach with a decision tree
# Then once you're clear on the decision tree 'forward' approach with O(N) space complexity, then you can reverse it to get the iterative bottom-up approach
class Solution_V2:
    def numDecodings(self, s: str) -> int:
        prev_resp, resp = 1, 1
        for i in range(len(s) - 1, -1, -1):
            # 0 -> Current decision subtree dies
            if s[i] == "0":
                prev_resp = resp
                resp = 0
            # If join, merge two decision subtrees
            elif i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                tmp = resp
                resp += prev_resp
                prev_resp = tmp
            # No join, extend current decision subtree
            else:
                prev_resp = resp
        return resp

# Ok this is a much simpler implementation than mine, but it is O(N) storage
# Have to use O(N) storage if you start from the start, can improve to O(1) storage if start from the back
# Sort of nice to do it in a single recursive function with two decisions
# Base cases
    # i.) current code == 0 which means the decision tree dies - return 0
    # ii.) Already memoized
    # iii.) Reached out of bounds - return 1
# Decisions
    # i.) No join -> reduce to i + 1
    # ii.) Join -> reduce to i + 2
# Ok should be able to implement O(1) iterative backwards, with this clarified understanding
class Solution_AfterNeetV1:
    def numDecodings(self, s: str) -> int:
        dp = {}

        # DFS going forward
        # Ok this is a decision tree starting from the first character
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if i >= len(s):
                return 1

            # No combo on 0 - all decision trees die at 0
            if s[i] == "0":
                return 0
            
            # Default case - no join
            resp = dfs(i + 1)

            # Can join on next
            if i + 1 < len(s) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456")):
                resp += dfs(i + 2)

            dp[i] = resp
            return resp

        return dfs(0)

class Solution_NeetV1:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }

        # DFS going forward
        def dfs(i):
            if i in dp:
                return dp[i]
            # No combo on 0
            if s[i] == "0":
                return 0
            
            # No join
            resp = dfs(i + 1)

            # Can join on next
            if i + 1 < len(s) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456")):
                resp += dfs(i + 2)

            dp[i] = resp
            return resp

        return dfs(0)


# Hmm so legitimate codings are 1 to 26
# Ok took like 1.5hrs to solve this problem without any help...mmm think I went down the wrong rabbit hole here and there must be a simpler solution
# 87% runtime, 47% memory on Leetcode, but took way too long to solve this
# Ok the good thing is that I came up with the most efficient solution - O(N) time efficiency, O(1) space efficiency, iterative and using DP
# Bad news is that it took way too long to even come up with a working solution
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        if len(s) == "1":
            return 1

        prev_resp, resp = 1, 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "1":
                # No join
                if i+2 < len(s) and s[i+2] == "0":
                    prev_resp = resp
                    resp = resp
                # Join
                elif s[i + 1] != "0":
                    tmp = resp
                    resp += prev_resp
                    prev_resp = tmp
                # No join
                else:
                    prev_resp = resp
                    resp = resp
            elif s[i] == "2":
                # No join
                if i+2 < len(s) and s[i+2] == "0":
                    prev_resp = resp
                    resp = resp
                # No join
                elif int(s[i+1]) > 6 or s[i+1] == "0":
                    prev_resp = resp
                    resp = resp
                # Join
                else:
                    tmp = resp
                    resp += prev_resp
                    prev_resp = tmp
            # 0 - 9
            else:
                # Edge case, not allowed
                if s[i + 1] == "0":
                    return 0
                # No join
                else:
                    prev_resp = resp
                    resp = resp

        return resp

sln = Solution_V2()
print(sln.numDecodings("12")) #2
print(sln.numDecodings("01")) #0
print(sln.numDecodings("1012")) #2
print(sln.numDecodings("101012")) #2
print(sln.numDecodings("221012")) #4
print(sln.numDecodings("226")) #3
print(sln.numDecodings("2226")) #5


# 12 - 1 2, or 12
# 01 - no
# 1012 - 10 12, 10 1 2

# Left pass - start from X
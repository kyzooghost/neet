# Hmm, the '*' is the interesting part because it can be anything
# '(' = push onto stack
# ')' = pop off stack
# T = Stack empty, F = Stack not empty
# So * -> 3 possibilities
# You can brute force this by backtracking, and creating 3 branches at each *
# But early exit if too many (, count of ( must <= len(s) / 2
# Let's implement brute force first

# Hmm so 2D DP where DP[i,j] is for i = index, j = l_count
# Works, but implementation is annoying af and get 12% runtime and 5% memory
class Solution_DP:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        
        def backtrack(i, leftCount):
            if (i, leftCount) in dp: return dp[(i, leftCount)]
            if leftCount < 0: return False
            if i >= len(s):
                resp = leftCount == 0
                dp[(i, leftCount)] = resp
                return resp
            
            char = s[i]
            resp = False
            if char == '(':
                leftCount += 1
                resp |= backtrack(i + 1, leftCount)
                if resp:
                    dp[(i, leftCount)] = resp
                    return resp
                leftCount -= 1
            elif char == ')':
                leftCount -= 1
                resp |= backtrack(i + 1, leftCount)
                if resp:
                    dp[(i, leftCount)] = resp
                    return resp
                leftCount += 1
            else:
                # (
                leftCount += 1
                resp |= backtrack(i + 1, leftCount)
                if resp:
                    dp[(i, leftCount)] = resp
                    return resp
                leftCount -= 1
                # )
                leftCount -= 1
                resp |= backtrack(i + 1, leftCount)
                if resp:
                    dp[(i, leftCount)] = resp
                    return resp
                leftCount += 1
                # _
                resp |= backtrack(i + 1, leftCount)
                
            dp[(i, leftCount)] = resp
            return resp

        return backtrack(0, 0)

# Ok watched Neet, it is basically the same as Solution3 except we use a variable instead of a stack
# Still 100% runtime, 11-18% memory
class Solution_Neet_Greedy:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                leftMax += 1
                leftMin += 1
            elif char == ')':
                leftMax -= 1
                leftMin -= 1
            else:
                leftMax += 1
                leftMin -= 1
            
            if leftMax < 0: return False
            if leftMin < 0: leftMin = 0

        return leftMin == 0

# Ok I read a few discussion comments
# Still not sure about 2D DP, but we could do an 'optimistic' stack and a 'pessimistic' stack
# Optimistic means assume (, pessimistic means assume )
# Damn this worked for Neetcode @ 50 mins. No DP, and iterating with 2 stacks rather than classic backtracking
# Ooft, 100% runtime and 14% memory
class Solution3:
    def checkValidString(self, s: str) -> bool:
        MAGIC_STACK_CONTENT = 'X'
        assume_append_stack = []
        assume_pop_stack = []

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                assume_append_stack.append(MAGIC_STACK_CONTENT)
                assume_pop_stack.append(MAGIC_STACK_CONTENT)
            elif char == ')':
                if len(assume_append_stack) == 0: return False
                assume_append_stack.pop()
                if len(assume_pop_stack) > 0: assume_pop_stack.pop()
            else:
                assume_append_stack.append(MAGIC_STACK_CONTENT)
                if len(assume_pop_stack) > 0: assume_pop_stack.pop()

        return len(assume_pop_stack) == 0

# Damn, 27 mins here and failed on case 8/23 for Neet
# Ok opened the Leetcode hints, the ones I haven't accounted for are: use 2 stacks + use 2D DP
# Hmm they still encourage backtrack hmmm...I guess if backtrack returns True, you can return straight away
# But still get TLE with early returns
# Hmm how would DP help, if DP[i,j] is true, then you only need to figure out if DP[0,i-1] and Dp[j+1,len(s)] is true
# Then does that mean we start from the middle, rather than from one end of the string?
class Solution2:
    def checkValidString(self, s: str) -> bool:
        MAGIC_STACK_CONTENT = 'X'
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(MAGIC_STACK_CONTENT)
            elif char == ')':
                if len(stack) == 0: return False
                stack.pop()
            else:
                REMAINING_CHARS = len(s) - i
                DIFFERENCE = REMAINING_CHARS - len(stack) - 1
                # Use as blank
                if DIFFERENCE == 0:
                    pass
                elif DIFFERENCE > 0:
                    stack.append(MAGIC_STACK_CONTENT)
                else:
                    stack.pop()

        return len(stack) == 0        

# Lol TLE even for Neet, @ 15 mins
# So how can you be greedy here? What greedy algorithm can you use for the *?
# Hmm, so you can partition 's' into before, middle and after
# Params = current stack size, and remaining character in 's'
# If cur stack size > remaining characters, early return false
class Solution:
    def checkValidString(self, s: str) -> bool:
        MAGIC_STACK_CONTENT = 'X'
        stack = []

        def backtrack(i, stack):
            if i >= len(s): return len(stack) == 0
            char = s[i]
            resp = False
            if char == '(':
                stack.append(MAGIC_STACK_CONTENT)
                resp |= backtrack(i + 1, stack)
                if resp: return resp
                stack.pop()
            elif char == ')':
                if len(stack) == 0: return False
                stack.pop()
                resp |= backtrack(i + 1, stack)
                if resp: return resp
                stack.append(MAGIC_STACK_CONTENT)
            else:
                # (
                stack.append(MAGIC_STACK_CONTENT)
                resp |= backtrack(i + 1, stack)
                if resp: return resp
                stack.pop()
                # )
                if len(stack) > 0:
                    stack.pop()
                    resp |= backtrack(i + 1, stack)
                    if resp: return resp
                    stack.append(MAGIC_STACK_CONTENT)
                # _
                resp |= backtrack(i + 1, stack)
            
            return resp

        return backtrack(0, stack)

sln = Solution_DP()
print(sln.checkValidString("((**)"))
print(sln.checkValidString("(((*)"))  
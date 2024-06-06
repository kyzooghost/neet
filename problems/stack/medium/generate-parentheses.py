# Alright let's try to solve this with backtracking
# Different permutation of push and pop, hmmm
# Push -> add '(', pop -> add ')'
# Limits for push and pop, push limited by open left, pop is limited to stack
# 79% runtime, 65% memory
# Nice, got this for first submission
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.resp = []
        def backtrack(cur_string, remaining_push, stack_len):
            if remaining_push == 0 and stack_len == 0:
                self.resp.append(cur_string)
                return
            # Push path
            if remaining_push > 0:
                backtrack(cur_string + '(', remaining_push - 1, stack_len + 1)
            # Pop path
            if stack_len > 0:
                backtrack(cur_string + ')', remaining_push, stack_len - 1)

        backtrack('', n, 0)
        return self.resp

sln = Solution()
print(sln.generateParenthesis(1))
print(sln.generateParenthesis(2))
print(sln.generateParenthesis(3))


        
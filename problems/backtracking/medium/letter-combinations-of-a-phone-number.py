
# This looks like a straightforward backtracking problem
# 76% runtime, 68% memory in 14 minutes. Yay did a medium in reasonable time for once. Or maybe this just feels light because I've just been doing hards for the last few questions.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        chars = {}
        for i in range(2, 7):
            chars[str(i)] = []
            ascii_code_start = ord("a") + (i - 2) * 3
            for j in range(0, 3):
                chars[str(i)].append(chr(ascii_code_start + j))
        chars["7"] =["p", "q", "r", "s"]
        chars["8"] =["t", "u", "v"]
        chars["9"] =["w", "x", "y", "z"]

        resp = []

        def backtrack(i, prev_string):
            if i == len(digits):
                resp.append(prev_string)
                return
            for letter in chars[digits[i]]:
                backtrack(i+1, prev_string[:] + letter)

        backtrack(0, "")
        return resp
        
sln = Solution()
print(sln.letterCombinations("2"))
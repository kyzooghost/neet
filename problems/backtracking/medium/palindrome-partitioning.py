

# All possible lists of substrings
# Single letter by itself is a substring
# Cool, 40% runtime, 51% memory in 17.5 minutes. But zz got hit by a silly edge case
# O(2 ** n)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        resp = []

        def is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        def backtrack(i, j, temp_resp):
            # Not a palindrome, return
            if is_palindrome(i, j) is False:
                return
            
            # is_palindrome, append
            temp_resp.append(s[i:j+1])
            print(s[i:j+1], resp, temp_resp)

            # Reached end, return
            if j == len(s) - 1:
                resp.append(temp_resp[:])
                temp_resp.pop()
                return

            for next_j in range(j + 1, len(s)):
                backtrack(j+1, next_j, temp_resp)

            temp_resp.pop()

        for j in range(0, len(s)):
            backtrack(0, j, [])

        return resp

sln = Solution()
# print(sln.partition("aab"))
# print(sln.partition("a"))
print(sln.partition("cdd"))


# Well, this is the exact same approach as for longest palindromic substring
# We are still using O(N^2) time and O(1) space
# Not sure how we could achieve O(N lg N) or even O(N) time
class Solution:
    def countSubstrings(self, s: str) -> int:
        resp = 0
        for i in range(len(s)):
            # Odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                resp += 1
                l -= 1
                r += 1
            # Even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                resp += 1
                l -= 1
                r += 1

        return resp

sln = Solution()
print(sln.countSubstrings("aaa"))
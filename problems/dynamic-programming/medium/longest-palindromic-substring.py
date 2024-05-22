
from collections import defaultdict

class Solution_AfterWatchNeet:
    # Oh, Neet's solution is not that satisfying. I thought this problem had an O(N) time complexity solution because all the prior DP problems I have been doing had an O(N) solution. But seems like it is still O(N^2)
    # 51% runtime, 30% memory
    # Well I prefer Neet's solution - much simpler to explain and implement, and same time complexity as my solution. My sotution also has O(N) space complexity whereas Neet's does not.
    def longestPalindrome(self, s: str) -> str:
        resp = ""

        for i in range(len(s)):
            # Check for odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(resp):
                    resp = s[l:r+1]
                l -= 1
                r += 1

            # Check for even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(resp):
                    resp = s[l:r+1]
                l -= 1
                r += 1

        return resp
    
# Urgh, took 1 hr to come up with a shitty brute force solution. Kept trying to find a neater solution with better time efficiency, but couldn't do it lol. So this solution is O(N^2) and there is no real dynamic programming element to this implementation
# Well this brute force was accepted with 30% runtime, and 48% memory lol
# In a real interview, I should just smash out the brute force with time complexity first. Give maybe 5 minutes to see if I can come up with a better time complexity solution, if not smash out the brute force.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        resp = s[0]
        self.positions = defaultdict(list)
        self.positions[s[0]].append(0)

        def is_palindrome(s):
            if len(s) == 0 or len(s) == 1: return True
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        # Look backwards for a larger palindrome, stop when impossible
        # Need to find self
        for i in range(1, len(s)):
            if s[i] in self.positions:
                for index in self.positions[s[i]]:
                    if i - index + 1 <= len(resp):
                        break
                    else:
                        if is_palindrome(s[index:i+1]):
                            resp = s[index:i+1]

            self.positions[s[i]].append(i)
        return resp

sln = Solution_AfterWatchNeet()
print(sln.longestPalindrome("ababd"))
print(sln.longestPalindrome("abbc"))

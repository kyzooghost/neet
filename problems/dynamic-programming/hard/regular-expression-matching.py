# String s
# Pattern p - '.' -> Any single character
# '*' -> 0 or more of the entire string
# Entire input string match
# Only lowercase English letters

# In terms of 2D DP, you can clearly reduce this by index in the strings
# Match entire string, the challenge here is '*' - when do you stop repeating?
# Each appearance of '*', will be preceded by a valid character or '.'

# Ah shit...can be 0 or more hmm...so can wipe out 
# Fek...just consider * as block of two

# Ok two more breakthroughs from watching Neet
# 1 - Base case is actually both s_i and p_i out of bounds at same time. And you need to tolerate the s_i out of bounds case here.
# 2 - Use hashmap, not 2D array with fixed dimensions, because we need to support s_i out of bounds
# 95% runtime, 12% memory
class Solution_Neet(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = {}

        def _is_match(s_i, p_i):
            if s_i > len(s) - 1: return False
            s_char, p_char = s[s_i], p[p_i]
            if p_char == ".": return True
            if s_char == p_char: return True
            return False

        def _is_wildcard_after(p_i):
            if p_i >= len(p) - 1: return False
            return p[p_i + 1] == "*"

        def recurse(s_i, p_i):
            if ((s_i, p_i) in dp): return dp[(s_i, p_i)]
            if s_i >= len(s) and p_i >= len(p): return True
            if p_i >= len(p): return False

            # s_i can still be out of bounds
            is_wildcard_after = _is_wildcard_after(p_i)
            is_match = _is_match(s_i, p_i)
            resp = False

            if is_wildcard_after == True:
                resp = resp or recurse(s_i, p_i + 2)
                if is_match: resp = resp or recurse(s_i + 1, p_i)
            else:
                if is_match: resp = resp or recurse(s_i + 1, p_i + 1)

            dp[(s_i, p_i)] = resp
            return resp
        return recurse(0, 0)

# Goddam, took 2 hrs 45 minutes to get first submission on Leetcode - 48% runtime, 12% memory
# * character match was really tricky here, especially the edge case that it can represent '0' of the preceding character
# The edge cases that come from that zzzz
# The breakthrough for me was to never consider '*' as a single state transition, but '.*' as the single state transition
class Solution_V2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[None for _ in range(len(p))] for _ in range(len(s))]

        def _is_match(s_char, p_char):
            if s_char == p_char: return True
            if p_char == ".": return True
            return False

        def _is_wildcard_after(p_i):
            if p_i >= len(p) - 1: return False
            return p[p_i + 1] == "*"

        def recurse(s_i, p_i):          
            if s_i > len(s) or p_i >= len(p): return False
            is_wildcard_after = _is_wildcard_after(p_i)

            if s_i == len(s):
                if is_wildcard_after == False: return False
                else:
                    if p_i == len(p) - 2: return True
                    else: return recurse(s_i, p_i + 2)

            if dp[s_i][p_i] is not None: return dp[s_i][p_i]

            is_match = _is_match(s[s_i], p[p_i])
            resp = False
            
            # Count 0 for current p_i
            if is_wildcard_after == True: resp = resp or recurse(s_i, p_i + 2)

            if is_match == True:
                if s_i == len(s) - 1:
                    if p_i == len(p) - 1: resp = True
                    elif p_i == len(p) - 2 and is_wildcard_after == True: resp = True
                if is_wildcard_after == False:
                    # Count 1
                    resp = resp or recurse(s_i + 1, p_i + 1)
                else:
                    # Count 1, skip *
                    resp = resp or recurse(s_i + 1, p_i + 2)
                    # Count +1
                    resp = resp or recurse(s_i + 1, p_i)
            else:
                resp = resp or False

            dp[s_i][p_i] = resp
            return resp
        
        return recurse(0, 0)

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[None for _ in range(len(p))] for _ in range(len(s))]

        def get_matching_p_char(p_i):
            p_char = p[p_i]
            # Relies on restriction that '*' is preceded only by lower English letter or '.'
            if p_char == "*": return p[p_i - 1]
            else: return p_char

        def is_match(s_char, p_char):
            if s_char == p_char: return True
            if p_char == ".": return True
            return False
        
        def is_wildcard_after(p_i):
            if p_i >= len(p) - 1: return False
            return p[p_i + 1] == "*"

        # Each recursion -> add s_i
        def recurse(s_i, p_i):
            # print(s_i, p_i)
            # Out of bounds
            if s_i >= len(s) or p_i >= len(p): return False
            # Already found in dp
            if dp[s_i][p_i] is not None: return dp[s_i][p_i]

            matching_s_char = s[s_i]
            matching_p_char = get_matching_p_char(p_i)
            is_wildcard = p[p_i] == "*"
            resp = False

            # Not match
            if is_match(matching_s_char, matching_p_char) == False:
                if is_wildcard_after(p_i) == True: resp = resp or recurse(s_i, p_i + 2)
                elif is_wildcard == True: resp = resp or recurse(s_i, p_i + 1)
                else: resp = False
            # Match
            else:
                # Reached terminal characters - recursion base case
                if s_i == len(s) - 1 and p_i == len(p) - 1: resp = True
                elif s_i == len(s) - 1 and p_i == len(p) - 2 and is_wildcard_after(p_i): resp = True
                elif s_i == len(s) - 1 and p_i == len(p) - 3 and is_wildcard_after(p_i + 1): resp = True
                elif s_i == len(s) - 1 and is_wildcard_after(p_i + 1): resp = resp or recurse(s_i, p_i + 2)
                # Much do further recursion
                else:
                    resp = resp or recurse(s_i + 1, p_i + 1)
                    if is_wildcard_after(p_i): resp = resp or recurse(s_i, p_i + 2)
                    if is_wildcard:
                        resp = resp or recurse(s_i + 1, p_i)
                        resp = resp or recurse(s_i, p_i + 1)

            dp[s_i][p_i] = resp
            return resp

        return recurse(0, 0)

sln = Solution_Neet()
print(sln.isMatch("xyz", ".*z"))
print(sln.isMatch("nnn", "n*"))
print(sln.isMatch("aa", ".b"))
print(sln.isMatch("aab", "c*a*b"))
print(sln.isMatch("aaa", "ab*a*c*a"))
print(sln.isMatch("aaca", "ab*a*c*a"))
print(sln.isMatch("a", "ab*"))
print(sln.isMatch("ab", ".*.."))
print(sln.isMatch("abb", "a.*b"))
print(sln.isMatch("bb", "..*c"))
print(sln.isMatch("a", ".*"))
print(sln.isMatch("a", "ab*b*"))
print(sln.isMatch("abc", ".*"))
print(sln.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*"))

# True
# True
# False
# True
# True
# True
# True
# True
# True
# False
# True
# True


# True
# print(sln.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*"))




# aca
# a*c*a


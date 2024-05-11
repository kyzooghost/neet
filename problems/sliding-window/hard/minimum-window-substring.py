# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included in the window. If there is no such # substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Err...O(M+N) will probably require KMP, which I don't know about currently
# So any permutation of t
# Substring of S -> use sliding windows here

# We know the substring of s must be >= len(t)
# Brute force is to see if any len(t) sliding window has the substring, then if any len(t) + 1 sliding window has it
# But how do we check if a window of s, contains any permutation of t?

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        resp = ""
        if len(t) > len(s):
            return resp
        
        # Populate t_dict
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        window_size = len(t)
        
        # O(M) subroutine
        def is_contain_t(dict):
            for char, count in t_dict.items():
                if dict.get(char, 0) < count:
                    return False
            return True

        # O(N) Outer loop for incrementing window size
        while window_size <= len(s):
            l, r = 0, window_size - 1
            # Get initial dict for this window
            dict = {}
            for i in range(r):
                dict[s[i]] = dict.get(s[i], 0) + 1

            # O(N) Inner loop for shifting window
            while r < len(s):
                dict[s[r]] = dict.get(s[r], 0) + 1
                # Check if current window has substring match
                if is_contain_t(dict) == True:
                    return s[l:r + 1]

                # Update shifting window
                dict[s[l]] -= 1
                l += 1
                r += 1

            window_size += 1

        return resp
        
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("a", "a"))
print(solution.minWindow("a", "aa"))


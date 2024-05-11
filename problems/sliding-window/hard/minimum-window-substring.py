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
    # 27 minutes to come up with O(M^2 * N) solution that passes 265/268 cases and gets Time Limit Exceeded lol
    # Can I use sliding windows instead of a nested for loop to make an O(MN) solution?
    # Well, sliding window is O(N) and this I have implemented optimized brute force which is still O(N^2)
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
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
        
        return ""

    # Use the Leetcode website hints of how to move the sliding windows
    # 5% runtime, 80% memory
    # O(MN) - N for sliding window, M for substring search
    def minWindow_v1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        resp = ""
        min_length = 10**5
        if len(t) > len(s):
            return resp
        
        # Populate t_dict
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        min_window_size = len(t)
        
        # O(M) subroutine
        def is_contain_t(dict):
            for char, count in t_dict.items():
                if dict.get(char, 0) < count:
                    return False
            return True
        
        l, r = 0, 0

        current_dict = {}

        # Shift right pointer until we have covered all characters in it
        while r < len(s):
            current_dict[s[r]] = current_dict.get(s[r], 0) + 1

            # Shift left pointer while we have covered all characters in t
            while l < r - min_window_size + 1 and is_contain_t(current_dict) == True:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    resp = s[l:r + 1]
                
                current_dict[s[l]] -= 1
                l += 1

            if is_contain_t(current_dict) == True and r - l + 1 < min_length:
                min_length = r - l + 1
                resp = s[l:r + 1]

            r += 1

        return resp

solution = Solution()
print(solution.minWindow_v1("ADOBECODEBANC", "ABC"))
print(solution.minWindow("a", "a"))
print(solution.minWindow("a", "aa"))
print(solution.minWindow_v1("ab", "b"))


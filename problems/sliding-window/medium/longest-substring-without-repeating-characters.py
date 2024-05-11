# Given a string s, find the length of the longest substring without repeating characters.

# Ummm, this feels easy, you just slide the pointers along the entire string until you get to the end

class Solution(object):

    # 83% runtime, 80% space
    def lengthOfLongestSubstring_v1(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        char_set = set()
        l, r = 0, 0
        resp = 0
        while r < length:
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            resp = max(resp, r - l + 1)
            r += 1
        return resp
    

    
    # Hmm 74% runtime, 18% memory
    # Implementation is much easier here - same general idea of sliding window
    # What did I trip up on?
        # Tripped up for at least 10 minutes on how to initialize and progress the main loop
            # Main loop can just be right pointer shift, and it is ok for right pointer to start at 0
            # Was very fixated on having the right pointer start at 1
        # Doing an if-else clause within the main loop, and then a while loop inside the else clause
            # Should define what happens in every loop - right pointer shift, add right pointer to set
            # Then the check if the right pointer char is already in the set
            # If in set, keep shifting left pointer and removing left pointer char from set. Add back duplicate after in happy case
            # For crossover edge case? Well char_set will be empty, so will not trigger while loop
    def lengthOfLongestSubstring_Neet(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_set = set()
        l = 0
        res = 0

        # Hmm, again this right pointer is moved by the outer loop and right pointer starts at 0
        # What do you do in this loop?
        for r in range(len(s)):
            # Encounter repeat - remove (l) from char, increment l pointer
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # Add (r) to char, increment r pointer
            char_set.add(s[r])
            # res = max(res, char_set) also works
            res = max(res, r - l + 1)    
        return res

# print(solution.lengthOfLongestSubstring("abcabcbb"))
# print(solution.lengthOfLongestSubstring("bbbbb"))
# print(solution.lengthOfLongestSubstring("pwwkew"))

    # Ok was really frustrated, did this by myself in 40 minutes. Was expecting to do it much under 30 minutes
    # I had the correct solution in the first minute or so, but I kept tripping over the edge cases and how to update the pointers
    # 25% runtime, 80% memory on first attempt
    # 60% runtime, 93% memory with a little tweaking
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        # Edge cases - 0
        if length == 0:
            return 0
        
        l, r = 0, 0
        char_set = set()
        char_set.add(s[l])
        resp = 1
        
        # Biggest place where I was stuck was the role of this while loop
            # Outer loop for right pointer shift
            # Inner loop for left pointer shift, and make sure left pointer cannot cross right pointer
        while r < length - 1:
            r += 1
            # If not repeating character, move right pointer
            if s[r] not in char_set:
                char_set.add(s[r])
                resp = max(len(char_set), resp)
            # Reached repeat, must move left pointer past repeated character
            else:
                # Once reach repeat, must move left pointer past repeated character
                while s[l] != s[r] and l < r:
                    char_set.remove(s[l])
                    l += 1
                l += 1
        return resp
        
solution = Solution()
print(solution.lengthOfLongestSubstring_v1("abcabcbb"))
print(solution.lengthOfLongestSubstring_v1("bbbbb"))
print(solution.lengthOfLongestSubstring_v1("pwwkew"))
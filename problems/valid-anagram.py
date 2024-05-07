# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Can use a hashmap again to store and compare the frequency of each character in s and t - O(N) space efficiency, O(N) time efficiency

# Another approach is to sort the strings then compare - O(1) space efficiency if we use in-memory sort, string sort may not neccesarily be O(N lg N) time efficiency.
# I am reading about count sort which offers O(N) space efficiency

class Solution(object):
    # Hashmap solution - O(N) time efficiency, O(N) space efficiency
    def isAnagram_Hashmap(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # O(N) space & O(N) time efficiency
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        # O(N) space & O(N) time efficiency
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        # Now compare the hashmaps - O(N) time efficiency
        for key, value in s_dict.items():
            if key not in t_dict:
                return False
            if t_dict[key] != value:
                return False
        
        return True

        # Overall O(N) space efficiency and O(N) time efficiency
        # Two edge cases to note here
        #   1. If len(s) < len(t), don't do any key-value pair comparison and straightaway return alse
        #   2. Must do None check for Python dict before trying to access - `if key not in dict:`


solution = Solution()
result = solution.isAnagram("rat", "car")
print(result)
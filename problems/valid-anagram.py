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

    def isAnagram_CountSort(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Nice O(N) (or O(1) if String is implemented as an object with a convenient count property) time efficiency escape clause
        if len(s) != len(t):
            return False

        s_ascii_max = 0
        t_ascii_max = 0

        # O(N) time efficiency, O(1) space efficiency - In the one for-loop, cast characters into ASCII code and find max element for each string
        for i in range(len(s)):
            s_ascii = ord(s[i])
            t_ascii = ord(t[i])
            s[i] = s_ascii
            t[i] = t_ascii
            if s_ascii > s_ascii_max:
                s_ascii_max = s_ascii
            if t_ascii > t_ascii_max:
                t_ascii_max = t_ascii

        # Another escape clause
        if s_ascii_max != t_ascii_max:
            return False

        # O(M) space efficiency, where M == max(s_ascii_max, t_ascii_max)
        s_countArray = [0] * (s_ascii_max + 1)
        t_countArray = [0] * (t_ascii_max + 1)

        # O(N) time efficiency to populate initial count array
        for ascii_code in s:
            s_countArray[ascii_code] += 1
        for ascii_code in t:
            t_countArray[ascii_code] += 1
        
        # O(N) time efficiency to store cumulative values
        for i in range(len(s)):
            

        # count_array

        


solution = Solution()
result = solution.isAnagram("rat", "car")
print(result)
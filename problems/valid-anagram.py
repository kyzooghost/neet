# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Can use a hashmap again to store and compare the frequency of each character in s and t - O(N) space efficiency, O(N) time efficiency

# Another approach is to sort the strings then compare - O(1) space efficiency if we use in-memory sort, string sort may not neccesarily be O(N lg N) time efficiency.
# I am reading about count sort which offers O(N) space efficiency

class Solution(object):
    # Seems like this offers the most convenient API, but Leetcode is not rewarding it - 48% percentile for time, 10% percentile for space 
    def isAnagram_HashmapImproved(self, s, t):
        if len(s) != len(t):
            return False

        # Nice syntax to declare multiple variables at the one time
        s_counter, t_counter = {}, {}

        # Populate counter
        for i in range(len(s)):
            # dict.get() - nice API to return default method instead of using two lines to do a `is None` check
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
            t_counter[t[i]] = 1 + t_counter.get(t[i], 0)

        # Iterate through counter
        for key in s_counter:
            if s_counter[key] != t_counter.get(key, 0):
                return False

        return True

    # Lmao at this too - well neither this nor the 'sorted' one-liner approches are rewarded in Leetcode
    # Counter is dict subclass (inherit from dict) - store object as keys and counts as values
    # https://realpython.com/python-counter/#getting-started-with-pythons-counter
    def isAnagram_Counter(self, s, t):
        return Counter(s) == Counter(t)

    # Lmao at this
    def isAnagram_Sort(self, s, t):
        # Timsort for Python 2.3-3.10, Powersort for 3.11
        # Time complexity - best case O(N), average & worst case O(N log N)
        # Space complexity - O(N)
        return sorted(s) == sorted(t)

    # Hashmap solution - O(N) time efficiency, O(N) space efficiency
    # 90th percentile for runtime and memory - Seemed to be penalized for dict.get() API
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
        for key in s_dict:
            if key not in t_dict:
                return False
            if t_dict[key] != s_dict[key]:
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

        s_ascii_list = []
        t_ascii_list = []
        s_ascii_max = 0
        t_ascii_max = 0

        # O(N) time efficiency, O(1) space efficiency - In the one for-loop, cast characters into ASCII code and find max element for each string
        for i in range(len(s)):
            s_ascii = ord(s[i])
            t_ascii = ord(t[i])
            s_ascii_list.append(s_ascii)
            t_ascii_list.append(t_ascii)
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
        for ascii_code in s_ascii_list:
            s_countArray[ascii_code] += 1
        for ascii_code in t_ascii_list:
            t_countArray[ascii_code] += 1

        # Don't actually need to do the entire count sort implementation, just need to get the countArray for both strings and compare them - still O(M + N) time and space efficiency, where N == max(len(s), len(t))
        for i in range(len(s_countArray)):
            if s_countArray[i] != t_countArray[i]:
                return False
        
        return True        

solution = Solution()
result = solution.isAnagram_HashmapImproved("ba", "ab")
print(result)
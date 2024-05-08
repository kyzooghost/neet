# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Hmm we know we can determine if two words are an anagram in O(N) time and space - we should use this as an internal function
# We need to start by forming the groupings, and not going backwards
# Then we need to go through the array, and figure out which grouping belongs

class Solution(object):
    # This solution is very bad lmao
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # length => List[AnagramGrouping]
        dict = {}
        id = 0

        # O(# of strings) time, iterate through each string and assign to a grouping
        for i in range(len(strs)):
            string = strs[i]
            length = len(string)

            # Definitely new anagram
            if length not in dict:
                new_grouping = AnagramGrouping(id, length, string)
                dict[length] = [new_grouping]
                id += 1
            else:
                found_anagram = False
                # Iterate through existing groupings in count
                for grouping in dict[length]:
                    # If match existing grouping, add to it - O(M + N space and time here)
                    # If doing this for each grouping - worst case O(# of strings * # of groupings * combined string length) time
                    example_string = grouping.strings[0]
                    if AnagramGrouping.isAnagram(example_string, string) == True:
                        grouping.add_string(string)
                        found_anagram = True
                        break

                if found_anagram == False:
                    # Else new anagram grouping
                    new_grouping = AnagramGrouping(id, length, string)
                    dict[length].append(new_grouping)
                    id += 1

        # Populate groupings - O(# of groupings found) - should not be significant time wise
        # O(total string count) space
        returned_groupings = []
        for key in dict:
            grouping_list = dict[key]
            for grouping in grouping_list:
                returned_groupings.append(grouping.strings)

        return returned_groupings
    
# O(total string count) space
class AnagramGrouping(object):
    def __init__(self, id, length, string):
        self.id = id
        self.length = length
        self.strings = [string]

    def add_string(self, string):
        self.strings.append(string)

    @staticmethod
    def isAnagram(s, t):
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

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))

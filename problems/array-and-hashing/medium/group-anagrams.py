# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Hmm we know we can determine if two words are an anagram in O(N) time and space - we should use this as an internal function
# We need to start by forming the groupings, and not going backwards
# Then we need to go through the array, and figure out which grouping belongs

class Solution(object):

    # Ok slightly better, getting 30-40% runtime and 25% memory. Mmmm...would rather do another question than try to optimize this further
    def groupAnagrams_v2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # So in Python, a list itself cannot be a map key, but a tuple of a list can
        # (frequencyCountArray) => [grouping]
        # dict = {}
        dict = {}

        # O(# of strings * length of strings)
        for current_string in strs:
            # Don't seem to be able to convert dict into a hashable key, so will need to use a list
            frequency_count = [0] * 26
            for current_character in current_string:
                frequency_count[ord(current_character) - ord("a")] += 1
            
            # Convert frequency_count into hashable form
            # Check for frequency count in dict
            # dict[tuple(frequency_count)].append(current_string)
            hash = tuple(frequency_count)
            if hash in dict:
                dict[hash].append(current_string)
            else:
                dict[hash] = [current_string]
        
        return dict.values()

    # Hmm yea ok the lessons here are
    # - In Python, you can use a tuple of a list as the dict key, but there doesn't seem to be a way to use a dict itself as a dict key
    #   - So the frequency_count list can be the dict key
    # - Use list(dict.values()) to cast into a list of the dict values

    # Big wrong ideas I had
    # - No need to use a class abstraction over the grouping - this is a code smell that the solution is getting too complicated
    # - Don't need to anchor to valid-anagram solution, in fact can use this solution for valid-anagram instead

    # Big correct ideas I had
    # - One single pass through 'strs'
    # - Store a list of strings for each anagram grouping, as a dict value
    # - We do want to use a representation of an anagram grouping to serve as the dict key, 

    # This solution is very bad lmao - <10% percentile for both runtime and memory
    # Had the correct general thoughts - but the implementation is bad
    # We still need a frequency count, but the entire frequency count itself can be the map key
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
print(solution.groupAnagrams_v2(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams_v2([""]))
print(solution.groupAnagrams_v2(["a"]))
print(solution.groupAnagrams_v2(["ddddddddddg","dgggggggggg"]))
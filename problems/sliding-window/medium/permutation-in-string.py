# Hmm - using a list instead of a hashmap?
# Lol Leetcode likes the sparse list of 26 vs dict - 68% runtime and 58% memory
# Ahh, it's O(26N) even with dict because is_substring_permutation is constant time operation
class Solution_V3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2): return False
        dict = [0 for _ in range(26)]
        for char in s1:
            char_index = ord(char) - ord("a")
            dict[char_index] += 1

        rolling_dict = [0 for _ in range(26)]
        l, r = 0, len(s1) - 1
        for i in range(l, r):
            char = s2[i]
            char_index = ord(char) - ord("a")
            rolling_dict[char_index] += 1
        
        def is_substring_permutation():
            for i in range(26):
                if rolling_dict[i] != dict[i]: return False
            return True

        while r < len(s2):
            l_char, r_char = s2[l], s2[r]
            l_char_index, r_char_index = ord(l_char) - ord("a"), ord(r_char) - ord("a")
            rolling_dict[r_char_index] += 1

            if dict[l_char_index] > 0 and dict[r_char_index] > 0:
                if is_substring_permutation(): return True
            rolling_dict[l_char_index] -= 1
            l += 1
            r += 1
        
        return False

# Ahh actually accepted by Leetcode, 25% runtime and 37% memory
# Definitely did this in under 30 minutes, didn't time how long
class Solution_V2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2): return False
        dict = {}
        for char in s1:
            dict[char] = dict.get(char, 0) + 1

        rolling_dict = {}
        l, r = 0, len(s1) - 1
        for i in range(l, r):
            char = s2[i]
            rolling_dict[char] = rolling_dict.get(char, 0) + 1
        
        def is_substring_permutation():
            for key in dict.keys():
                if key not in rolling_dict: return False
                if rolling_dict[key] != dict[key]: return False
            return True

        while r < len(s2):
            rolling_dict[s2[r]] = rolling_dict.get(s2[r], 0) + 1
            print(rolling_dict)

            if s2[l] in dict and s2[r] in dict:
                if is_substring_permutation(): return True
            rolling_dict[s2[l]] -= 1
            l += 1
            r += 1
        
        return False

sln = Solution_V3()
print(sln.checkInclusion("ab", "lecabee"))

# Hmm this was accepted by Neetcode but I don't think Leetcode will accept it - O(MN) time complexity because traverse across s2 (M) while doing substring comparison every time
# I think we should be able to optimise this to O(M) time complexity, by not reconstructing the substring_dict each time. Well...we need O(N) time to compare whether this is a substring or not. So still O(MN) time hmm
# Unless we can perform substring permutation comparision in O(1) time...
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2): return False

        dict = {}
        for char in s1:
            dict[char] = dict.get(char, 0) + 1

        def is_s1_permutation(substring):
            substring_dict = {}
            for char in substring:
                substring_dict[char] = substring_dict.get(char, 0) + 1
            for key in substring_dict.keys():
                if key not in dict: return False
                if substring_dict[key] != dict[key]: return False
            return True

        l, r = 0, len(s1) - 1
        while l < len(s2) and r < len(s2):
            if s2[l] in dict and s2[r] in dict:
                if is_s1_permutation(s2[l:r+1]): return True
            l += 1
            r += 1
            
        return False
        
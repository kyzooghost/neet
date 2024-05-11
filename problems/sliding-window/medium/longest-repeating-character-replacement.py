# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Sliding window base - l

from collections import defaultdict 

class Solution(object):
    # Ok took ~28 minutes to get to "Time Limit Exceeded", we have an O(N^2) time complexity implementation here because the R pointer can slide back to the L pointer
    # Can we do this without moving the R pointer backwards? I think yes, but I am thinking I would need to use a dict to store what characters I have already gone over
    # If R pointer can slide backwards, it is no longer a sliding window O(N) implementation and becomes O(N^2)
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        resp = 0
        length = len(s)

        l, r, replacements = 0, 0, k
        
        while r < length:
            if s[r] != s[l]:
                # Have replacements left - just go to next string
                if replacements != 0:
                    replacements -= 1
                else:
                    old_base = s[l]
                    while s[l] == old_base:
                        l += 1
                    r = l
                    replacements = k
            
            resp = max(resp, r - l + 1)
            r += 1

        resp = max(min(length, r - l + replacements), resp)

        return resp

    ### Urgh, must have tried for 2 hours but haven't been able to get it right.
    # Ok big mistake here is getting fixated on the left pointer being stable, rather than on evaluating the sliding window. When I am fixated on the left pointer being the character of choice, it means that I have to also account for the edge case
    # Got fixated on this approach because I could do the O(N^2) solution fairly quick for it. but even in O(N^2) implementation I have to account for edge case of characters being allowed on the left. It feels like the wrong focus for solving the specific problem, because there are edge cases that seem to awkwardly escape out of it
    # I am also having issues working with this extra variable - 'replacements'
    # Too many edge cases with using the 'constant L pointer' approach
        # Edge case of not exploring sequences stuck to the right
        # Edge cases of updating 'replacement' variable, leftover 'replacement' varaible
    
    # Sigh...took 3 hrs and looking at Neetcode solution, but got it for 61% runtime, 71% memory
    # This approach is just wrong - just way too many awkward edge cases to account for
    def characterReplacement_v1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        resp = 0
        length = len(s)

        l, r, replacements = 0, 0, k
        dict = {}
        
        def replacements_needed():
            return (r - l + 1) - dict[s[l]]

        while r < length:
            dict[s[r]] = dict.get(s[r], 0) + 1

            print(f"{l} {s[l]} -> {r} {s[r]}")

            # Based on s[l], use replacement if not same as base, otherwise must move l
            if s[r] != s[l]:
                if replacements > 0:
                    replacements -= 1
                else:
                    old_base = s[l]
                    while s[l] == old_base:
                        dict[s[l]] -= 1
                        l += 1

                    while replacements_needed() > k:
                        dict[s[l]] -= 1
                        l += 1

                    replacements = k - replacements_needed()

            resp = max(resp, r - l + 1)
            r += 1

        # Account for edge case of - squashed against right, but still can use left as replacements
        resp = max(min(length, r - l + replacements), resp)

        # Account for edge case of - squashed against right, but most frequent character is not the base
        # Get max count in count
        dict_max = 0
        for count in dict.values():
            dict_max = max(count, dict_max)
        resp = max(resp, min(length, dict_max + k))

        return resp
        
    # Sigh this sliding window is so much easier to implement
    # The sliding window is basically main R) pointer increment loop, and work out which condition to increment L) pointer in an inner loop
    # 6% runtime, 71% memory
    def characterReplacement_Neet(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        def get_max_count():
            max_count = 0
            for num in count.values():
                max_count = max(num, max_count)
            return max_count
        
        length = len(s)
        l, r = 0, 0
        resp = 0
        while r < length:
            count[s[r]] = count.get(s[r], 0) + 1
            while k + get_max_count() < r - l + 1:
                count[s[l]] -= 1
                l += 1

            resp = max(resp, r - l + 1)
            r += 1
        
        return resp


    def characterReplacement_NeetV2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        maxf = 0
        
        length = len(s)
        l, r = 0, 0
        resp = 0
        while r < length:
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while k + maxf < r - l + 1:
                count[s[l]] -= 1
                l += 1

            resp = max(resp, r - l + 1)
            r += 1
        
        return resp

solution = Solution()
# print(solution.characterReplacement_v1("ABAB", 2))
# print(solution.characterReplacement_v1("AABABBA", 1))
# print(solution.characterReplacement_v1("ABCDE", 1))
# print(solution.characterReplacement_v1("", 1))
# print(solution.characterReplacement_v1("ABBB", 1))
# print(solution.characterReplacement_v1("AAAB", 0))
# print(solution.characterReplacement_v1("BAAAB", 2))

# 6
print(solution.characterReplacement_NeetV2("ABCDDD", 3))

# 6
# print(solution.characterReplacement_v1("KRSCDCSONAJNHLBMDQGI", 4))

# 7
# print(solution.characterReplacement_v1("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))

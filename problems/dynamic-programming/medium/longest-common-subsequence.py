
# 54% runtime, 65% memory
class Solution_2DDP(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # Wrong - https://stackoverflow.com/a/44382900
        # dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[len(text1)][len(text2)]

# text1 = "abcdef", text2 = "abc"
sln = Solution_2DDP()
# print(sln.longestCommonSubsequence("ac", "cd"))
print(sln.longestCommonSubsequence("abcba", "abcbcba"))


# 1D O(N^2) implementation
# Ok failed on this test case - "mhunuzqrkzsnidwbun" and "szulspmhwpazoxijwbq"
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        longest = text1 if len(text1) > len(text2) else text2
        shortest = text2 if len(text1) > len(text2) else text1

        def is_subsequence_found(string, subsequence):
            i = 0
            for char in string:
                if subsequence[i] == char:
                    i += 1
                    if i == len(subsequence):
                        return True
            return False

        longest_subsequence = ""
        # Iterate backwards through shortest
        for i in range(len(shortest) - 1, -1, -1):
            # Iterate forward through longest to find subsequence
            if is_subsequence_found(longest, shortest[i] + longest_subsequence):
                longest_subsequence = shortest[i] + longest_subsequence
            elif len(longest_subsequence) > 0 and is_subsequence_found(longest, shortest[i] + longest_subsequence[1:]):
                longest_subsequence = shortest[i] + longest_subsequence[1:]

        longest_subsequence_2 = ""
        # Iterate forward through shortest
        for i in range(len(shortest)):
            if is_subsequence_found(longest, longest_subsequence_2 + shortest[i]):
                longest_subsequence_2 = longest_subsequence_2 + shortest[i]
            elif len(longest_subsequence_2) > 0 and (longest, longest_subsequence_2[0:len(longest_subsequence_2)-1] + shortest[i]):
                longest_subsequence_2 = longest_subsequence_2[0:len(longest_subsequence_2)-1] + shortest[i]

        return max(len(longest_subsequence), len(longest_subsequence_2))


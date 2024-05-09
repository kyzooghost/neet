# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

from typing import List

# Mmm, I don't understand the behaviour of .join and .split as it wasn't working for the edge cases of [] and ['']
# So I manually implemented what I was looking for in .join and .split and it worked
class Solution(object):
    def encode(self, strs: List[str]) -> str:
        delimiter = "\0"
        resp = ""
        for string in strs:
            resp += string
            resp += delimiter
        return resp
    
    def decode(self, s: str) -> List[str]:
        delimiter = "\0"
        resp = []

        current_word = ""
        for char in s:
            if char == delimiter:
                resp.append(current_word)
                current_word = ""
            else:
                current_word += char

        return resp

solution = Solution()

input1 = ["neet","code","love","you"]
input2 = ["we","say",":","yes"]
input3 = []
input4 = [""]

print(solution.decode(solution.encode(input1)))
print(solution.decode(solution.encode(input2)))
print(solution.decode(solution.encode(input3)))
print(solution.decode(solution.encode(input4)))
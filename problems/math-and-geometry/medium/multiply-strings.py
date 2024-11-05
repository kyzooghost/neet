# Lmao...handbuilt `int()` function improved to 8% runtime and 69% memory
# Then caching the 'i_multiplier' and 'j_multiplier' improved results to 45% runtime, 69% memory
# I don't think I did this according to strict rules - system may not be able to store int. 
# But it's still not a real problem because with a UTF-8 string you are using 1 byte per character -> *10 per byte
# With int it's *256 per byte, which is a 2.5x improvement in space efficiency to store the number
class Solution_V2:
    def multiply(self, num1: str, num2: str) -> str:
        str_to_num = {}
        j_multiplier = {}
        for i in range(10): str_to_num[str(i)] = i
        for j in range(len(num2)): j_multiplier[j] = 10 ** (len(num2) - 1 - j)
            
        resp = 0
        for i in range(len(num1) - 1, -1, -1):
            i_multiplier = 10 ** (len(num1) - 1 - i)
            for j in range(len(num2) - 1, -1, -1):
                i_num = str_to_num[num1[i]] * i_multiplier
                j_num = str_to_num[num2[j]] * j_multiplier[j]
                resp += i_num * j_num

        return str(resp)

# No use of built in library, or convert input to integer
# Err...what do you mean you cannot convert input to integer directly? You need to convert to integers at some point
# Well did in 15 minutes on Neetcode, accepted for Leetcode with 5% runtime and 14% memory
# Hmm...so this is O(M*N) where M = len(num1) and N = len(num2), the results are suggesting there is a more time efficient way to do this. Maybe O(M+N)?
# Can we do anything with bitwise operations?
# Lol removing the single print statement improved memory to 38%, but did nothing about runtime
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        resp = 0

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                i_num = int(num1[i]) * (10 ** (len(num1) - 1 - i))
                j_num = int(num2[j]) * (10 ** (len(num2) - 1 - j))
                resp += i_num * j_num

        return str(resp)

sln = Solution_V2()
print(sln.multiply("123", "456"))
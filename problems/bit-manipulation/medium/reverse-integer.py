import math
# 32-bit integer, return reversed integer
# Hmm you could tackle this as a string reverse operation and cover the edge cases
# How could you tackle as a bitwise operation?

# 100 - 0b1100100
# 10 - 1010
# 1 - 1

# 69 - 1000101
# 96 - 1100000

# 123 - 0b1111011
# 321 - 0b101000001

# Hmm...what would be the bitwise operation solution for this?
# Esp when the binary representation doesn't really care about radix 10 representation?
# Hmm ok, we did break the '64-bit' restriction with the string representation - 2**31 takes 10 bytes to store in UTF-8 encoding, and we only have 8-bytes
# Watched Neet solution, it still doesn't really involve bitwise operations zz
# Lol, get 5% runtime and 38% memory in Leetcode hahaha
class Solution_V2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -2147483648
        MAX = 2147483647
        resp = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if resp > MAX // 10 or resp < MIN // 10: return 0
            if resp == MAX // 10 and digit >= MAX % 10: return 0
            if resp == MIN // 10 and digit <= MIN % 10: return 0
            resp = (resp * 10) + digit

        return resp

# Edge cases - negative #, start with 0, outside of bounds
# Ok, got the string manipulation solution in 12 minutes - 63% runtime, 28% memory
# Damn, haven't done Leetcode in almost 2 weeks, feels great to do it again tbh
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            str_x = str(x)
            rev_str_x = str_x[::-1]
            # Out of bounds
            if int(rev_str_x) > 2**31 - 1: return 0
            i = 0
            # Iterate until 
            while rev_str_x[i] == 0:
                i += 1
            return int(rev_str_x[i::])
        # Address negative edge case
        elif x < 0:
            str_x = str(x)
            # Remove negative
            str_x = str_x[1::]
            rev_str_x = str_x[::-1]
            # Out of bounds
            if int(rev_str_x) > 2**31 - 1: return 0
            i = 0
            # Iterate until 
            while rev_str_x[i] == 0:
                i += 1
            return -int(rev_str_x[i::])
        else:
            return 0
        
sln = Solution_V2()
# print(sln.reverse(123))
print(sln.reverse(-120))

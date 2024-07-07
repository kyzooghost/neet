class Solution_V2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0:
            x = 1 / x
            n = -n
        resp = 1
        while n:
        # 0b1 = 1 -> * n
        # 0b10 = 2 -> * n^2
        # 0b11 = 3 -> n^2 * n
        # 0b100 = 4 -> n^4 * 1 * 1
            if n & 1:
                resp *= x
            x *= x
            n >>= 1
        return resp

# Hmm...this seems like a pure maths problem. I'm not familiar with how partial powers work
# n as an integer helps a lot
# x is between -100 and 100
# Hmm? Memory limit exceed for 291/306 test cases on Leetcode
# Use a bitmask to keep it within 32-bits I guess
# Ahh I see...the issue with this implementation is that the time complexity is O(N), where N <= 2^32
# So N is a 32-bit signed integer, so using bitwise operations we can bound this to O(1)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 32-bit bitmask
        if n > 0:
            resp = x
            for _ in range(n - 1):
                resp *= x
            return resp
        elif n < 0:
            resp = 1 / x
            for _ in range((-1 * n) - 1):
                resp *= (1 / x)
            return resp
        else:
            return 1

sln = Solution_V2()
print(sln.myPow(2.00000, 10))
print(sln.myPow(2.10000, 3))

print(sln.myPow(2.00000, -2))
print(sln.myPow(0.00001, 2147483647))

        
# n-1 -> removes 1 bit, n & (n-1) -> removes all new 1 bits created to the right
# So (num & num - 1) == 0 means the num had a single 1 bit -> is a power of 2
class Solution_NeetV2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        resp = 0
        while n:
            n &= (n-1)
            resp += 1
        return resp

# Oh, it's actually an O(1) time complexity - bounded by 32-bit number
class Solution_Neet(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        resp = 0
        while n:
            # %2 is the same as test if LSB is 1
            resp += n % 2
            # resp += n & 1
            n >>= 1
        return resp

# 12% runtime, 73% memory - well it works but probably not efficient enough lol
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        # Find MSB
        msb = 0
        while num > 0:
            num >>= 1
            msb += 1
        
        resp = 0
        # Check each bit from LSB to MSB
        for i in range(msb):
            if n & (1 << i) != 0:
                resp += 1

        return resp

sln = Solution_NeetV2()
print(sln.hammingWeight(11))
print(sln.hammingWeight(128))
print(sln.hammingWeight(2147483645))


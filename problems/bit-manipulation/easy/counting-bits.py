class Solution_AfterNeet_V2(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        resp = [0 for _ in range(n+1)]
        offset = 1
        for i in range(1, n+1):
            if offset << 1 == i: offset <<= 1
            resp[i] = 1 + resp[i - offset]
        return resp

class Solution_Neet(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if offset *2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

# 85% runtime, 95% memory
# Pretty clever DP solution mmm, no extra space required because the resp array is the DP array
class Solution_AfterNeet(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        if n == 1: return [0, 1]
        resp = [0, 1]
        cur_pow_of_2, next_pow_of_2 = 2, 4
        i = 2
        while i < n + 1:
            while i < n + 1 and i < next_pow_of_2:
                resp.append(1 + resp[i - cur_pow_of_2])
                i += 1
            cur_pow_of_2 <<= 1
            next_pow_of_2 <<= 1

        return resp

sln = Solution_AfterNeet_V2()
print(sln.countBits(4))

# I was wondering if there was a more efficient way to do this?
# 35% runtime, 93% memory - so this is not so bad
# No this is actually O(N lg N) - because the total amount of active bits to consider is lg N. Then why did Neet say for number-of-1-bits that it is an O(1) operation when it is actually O(lg N) lol
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        resp = []
        for i in range(n + 1):
            resp.append(self.hammingWeight(i))
        return resp

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
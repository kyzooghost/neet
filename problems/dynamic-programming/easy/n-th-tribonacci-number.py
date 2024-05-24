class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        x, y, z = 0, 1, 1

        for _ in range(3, n + 1):
            tmp = z
            z = x + y + z
            x = y
            y = tmp

        return z
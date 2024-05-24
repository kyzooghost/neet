class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        x, y = 0, 1

        for _ in range (2, n+1):
            tmp = y
            y = x + y
            x = tmp

        return y

        
# 50% runtime, 94% memory
# Gg must be tired, had the solution straight away but stuck with calling the wrong function for recursive call
class Solution_Iterative(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2

        n_minus_2, n_minus_1 = 1, 2
        for i in range(3, n):
            tmp1 = n_minus_1
            n_minus_1 = n_minus_1 + n_minus_2
            n_minus_2 = tmp1
        return n_minus_1 + n_minus_2

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.results = {}

        def recurse(n):
            if n == 1: return 1
            if n == 2: return 2
            if n in self.results: return self.results[n]
            result = recurse(n - 1) + recurse(n - 2)
            self.results[n] = result
            return result
        
        return recurse(n)
    
sln = Solution_Iterative()
print(sln.climbStairs(38))



        
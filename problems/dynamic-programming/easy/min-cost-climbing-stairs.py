class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2: return min(cost[0], cost[1])
        x, y = cost[0], cost[1]

        for i in range(2, len(cost)):
            tmp = y
            y = cost[i] + min(x, y)
            x = tmp

        return min(x, y)
    
sln = Solution()
print(sln.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

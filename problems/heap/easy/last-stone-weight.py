from heapq import heapify, heappop, heappush

# 100% runtime, 10% memory in 7 minutes
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)): stones[i] = -stones[i]
        heapify(stones)

        while len(stones) > 1:
            biggest = -heappop(stones)
            second_biggest = -heappop(stones)
            if biggest > second_biggest:
                heappush(stones, -(biggest - second_biggest))
        
        return -stones[0] if stones else 0


sln = Solution()
print(sln.lastStoneWeight([2,7,4,1,8,1]))
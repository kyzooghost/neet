from heapq import heappush, heappop

# Straightforward heap Q
# Finished in under 5 minutes, 45% runtime, 35% memory
# heapify is O(N) amortized time, because not every element takes O(lg N) to put in the correct index
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        for x, y in points:
            dist_squared = x * x + y * y
            heappush(heap, (dist_squared, x, y))

        resp = []
        for _ in range(k):
            _, x, y = heappop(heap)
            resp.append([x, y])
        return resp

sln = Solution()
print(sln.kClosest([[3,3],[5,-1],[-2,4]], 2))
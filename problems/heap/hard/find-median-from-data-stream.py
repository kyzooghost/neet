from heapq import heappush, heappop

# Yay conceived and implemented the solution in 23 minutes
class MedianFinder(object):

    def __init__(self):
        self.count = 0
        # max_pq
        self.l_max_pq = []
        # min_pq
        self.r_min_pq = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if self.count == 0:
            heappush(self.l_max_pq, -num)
        # Odd, current median is on l_max_pq -> Need to add to r_min_pq
        elif self.count % 2 == 1:
            current_median = -self.l_max_pq[0]
            
            if num >= current_median:
                heappush(self.r_min_pq, num)
            # Shift L max to R PQ
            else:
                tmp = -heappop(self.l_max_pq)
                heappush(self.r_min_pq, tmp)
                heappush(self.l_max_pq, -num)
        # Even, add to l_min_pq
        else:
            l_max = -self.l_max_pq[0]
            r_min = self.r_min_pq[0]

            if num <= r_min:
                heappush(self.l_max_pq, -num)
            else:
                tmp = heappop(self.r_min_pq)
                heappush(self.r_min_pq, num)
                heappush(self.l_max_pq, -tmp)
        self.count += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count % 2 == 0:
            return ( -self.l_max_pq[0] + self.r_min_pq[0] ) / 2.0
        else:
            return -self.l_max_pq[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
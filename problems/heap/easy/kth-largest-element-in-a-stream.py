from heapq import heapify, heappop, heappush


class KthLargest_Neet(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.queue = []
        self.k = k
        for num in nums:
            heappush(self.queue, num)
        while len(self.queue) > k:
            heappop(self.queue)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.queue) < self.k:
            heappush(self.queue, val)
            return self.queue[0]
        elif val > self.queue[0]:
            heappop(self.queue)
            heappush(self.queue, val)
            return self.queue[0]
        else:
            return self.queue[0]


# 16% runtime, 47% memory
# Damn, took 42 mins to come up with working solution - use a truncated min queue of length K lol
class KthLargest_V2(object):
    # Hmm, heap DS is fine - lg N addition
    # What if we have two heaps - the original one, and one that maintains X largest
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.queue = []
        self.add_initialized = False
        for num in nums:
            # Start as maximum queue
            heappush(self.queue, -num)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.add_initialized == False:
            # First call - guaranteed k numbers in self.queue
            heappush(self.queue, -val)
            # Make new min queue with k biggest numbers
            tmp = []
            for _ in range(self.k):
                heappush(tmp, -heappop(self.queue))
            self.queue = tmp
            # Smallest of k biggest numbers = k biggest number
            self.add_initialized = True
            return self.queue[0]
        else:
            prev_k_largest = self.queue[0]
            # Must enter into queue
            if val > prev_k_largest:
                heappop(self.queue)
                heappush(self.queue, val)
                return self.queue[0]
            else:
                return prev_k_largest

class KthLargest_V1(object):
    # Hmm, heap DS is fine - lg N addition
    # But how to maintain/find the k-th position?
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.queue = []
        self.k_num = float("-inf")
        for num in nums:
            heappush(self.queue, -num)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.queue, -val)

        if val > self.k_num:
            tmp = []
            for _ in range(self.k):
                tmp.append(heappop(self.queue))
            resp = -tmp[-1]
            for num in tmp:
                heappush(self.queue, num)
            self.k_num = resp
            return resp 
        else:
            return self.k_num

# Pass 9/10 than get TLE -> Ok, but not time efficient enough - O(N + K) space, O((N+K) lg N) time
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.queue = []
        for num in nums:
            heappush(self.queue, -num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.queue, -val)
        tmp = []
        for _ in range(self.k):
            tmp.append(heappop(self.queue))
        resp = -tmp[-1]
        for num in tmp:
            heappush(self.queue, num)
        return resp 

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
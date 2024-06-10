import math

# 70% runtime, 57% memory
class Solution_AfterNeet(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        max_piles = max(piles)
        if h == len(piles): return max_piles
        sum_piles = sum(piles)
        min_k = sum_piles // h
        if sum_piles % h > 0: min_k += 1
        l, r = min_k, max_piles

        resp = max_piles
        while l <= r:
            mid = (l + r) // 2

            hrs = 0
            for pile in piles:
                hrs += pile // mid
                if pile % mid > 0: hrs += 1
            if hrs <= h:
                resp = min(resp, mid)
                r = mid - 1
            else:
                l = mid + 1

        return resp

# Not sure why binary search is not getting memory limit exceeded, but brute force is?
# Is it the range(min_k, max_piles) iterator?
# Eih not happy with this one - took 1 hr to get a successful submission on Leetcode, 70% runtime and 12% memory
# I had like half the solution - min and max bound ideas, and O(N) function to determine if a given value was valid
# I wouldn't have thought to binary search within the solution space, I only saw examples where it was optimal to brute force from the min bound
# And the memory exceeded error mmm, didn't know using the range() iterator for a large range would consume much more memory than the equivalent while loop
# But yea, tripped up because thought there should be an O(lg N) solution or at least O(N), but O(N lg K)
# But yea, to be fair this is the first 'binary search within a solution space' problem I've encountered
# Every other binary search is literally binary search for an array element
class Solution_V4(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        max_piles = max(piles)
        if h == len(piles): return max_piles
        def can_eat(k):
            res = 0
            for pile in piles:
                res += pile // k
                if pile % k > 0: res += 1
            return res <= h

        # O(N)
        piles_sum = sum(piles)
        min_k = piles_sum // h
        if piles_sum % h > 0: min_k += 1

        l, r = min_k, max_piles

        mid = None
        while l <= r:
            mid = (l + r) // 2
            if can_eat(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        if can_eat(mid): return mid
        else: return mid + 1

class Solution_V3(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        max_piles = max(piles)
        if h == len(piles): return max_piles
        piles_sum = sum(piles)
        min_k = piles_sum // h
        if piles_sum % h > 0: min_k += 1
        
        i = min_k
        while i <= max_piles:
            res = 0
            for pile in piles:
                res += pile // i
                if pile % i > 0: res += 1
            if res <= h: return i
            i += 1


# Binary search within the solution space?
# Min_bound = sum // h + 1, # max_bound = 
class Solution_V2(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        max_piles = max(piles)
        if h == len(piles): return max_piles
        def can_eat(k):
            res = 0
            for pile in piles:
                res += pile // k
                if pile % k > 0: res += 1
            return res <= h

        # O(N)
        piles_sum = sum(piles)
        min_k = (piles_sum // h) + 1

        for i in range(min_k, max_piles):
            if can_eat(i):
                return i

# h >= piles.length
# Hmm not sure how this is a binary search Q
# Well a brute force way is iterating from 0, and finding values for h - This is O(h * len(piles))
# It is an O(len(piles)) subroutine to find the time for a given k
# Well the minimum bound is always sum // h, max bound is the largest element in piles
# if h == len(piles), you always use the largest element
# The answer is not neccessarily in the array
# What are we binary search for?
# Well got this shitty brute force solution in ~25 minutes. Memory limit exceeded on Leetcode lmao
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if h == len(piles): return max(piles)

        # O(N) subroutine
        def find_time(piles_, k_):
            res = 0
            print("hi")
            for pile in piles_:
                res += math.ceil(float(pile) / float(k_))
            return res

        # O(N)
        piles_sum = sum(piles)
        min_k = (piles_sum // h) + 1

        for i in range(min_k, max(piles)):
            if find_time(piles, i) <= h:
                return i

sln = Solution_AfterNeet()
# print(sln.minEatingSpeed([30,11,23,4,20], 6))
# print(sln.minEatingSpeed([3,6,7,11], 8))
# print(sln.minEatingSpeed([1000000000], 2))
print(sln.minEatingSpeed([312884470], 968709470))


# print(sln.minEatingSpeed([312884470], 312884469))

        

        
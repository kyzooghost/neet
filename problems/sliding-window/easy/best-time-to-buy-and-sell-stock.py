# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# You can brute force this in the similar way to container-with-most-water - Got O(N^2) in <7 minutes
# Should be able to achieve this in O(N)
# Profit = Max(prices[i + n] - prices[i])

class Solution(object):

    def maxProfit_v2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        resp = 0
        length = len(prices)
        l, r = length - 2, length - 1
        while l > -1:
            profit = prices[r] - prices[l]
            resp = max(profit, resp)
            if profit < 0:
                r = l
            l -= 1

        return resp

    # Urgh, this was an easy and couldn't find this one
    # 40% runtime, 42% memory
    # I had a number of two pointer solutions in mind, but none of them were correct
    # Ok what is the intuition here...you want the left pointer to be at the minimum
        # Start with l, r = 0, 1
        # Right pointer can do whatever, but if it finds something lower than L, update the left pointer to it
        # You start at the left side, so you prioritize optimising the left pointer - which should be at min
        # If you started at the right side, you do the opposite, prioritize the right pointer to be at max
    def maxProfit_v1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        resp = 0
        length = len(prices)
        l, r = 0, 1
        while r < length:
            profit = prices[r] - prices[l]
            resp = max(profit, resp)
            if profit < 0:
                l = r
            r += 1

        return resp

    # Trying every window length in every permutation = still O(N!), same as brute force really
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        l = 0
        resp = 0

        while l < length - 1:
            r = l + 1
            while r < length:
                profit = prices[r] - prices[l]
                resp = max(profit, resp)
                r += 1
            l += 1
        return resp


solution = Solution()
print(solution.maxProfit_v1([7,1,5,3,6,4]))
print(solution.maxProfit_v1([7,6,4,3,1]))
# 3
print(solution.maxProfit_v1([2,1,4]))
# 10
print(solution.maxProfit_v1([1,2,11,4,7]))
# 2
print(solution.maxProfit_v1([7,2,4,1]))
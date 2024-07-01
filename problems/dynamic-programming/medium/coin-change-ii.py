# I think this is almost the same as coin-change-i
# Ok...I don't know how long I took to get this question, did it over standup, so maybe did it in 40 minutes
# Runtime 27%, memory 25%, maybe ~40 minutes
# Definitely not the same as coin-change-i, the combinations requirement was a big adjustment
# But yay did this without hints
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0: return 0
        # cols - amount
        # rows - coin
        # dp = [[cols] * [rows]]
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        for coins_i in range(len(coins)):
            coin = coins[coins_i]
            for intermediate_amount in range(0, amount + 1):
                prev_amount = intermediate_amount - coin
                if prev_amount == 0:
                    dp[coins_i][intermediate_amount] += 1
                elif prev_amount > 0:
                    dp[coins_i][intermediate_amount] += dp[coins_i][prev_amount]
                
                if coins_i > 0:
                    dp[coins_i][intermediate_amount] += dp[coins_i - 1][intermediate_amount]

        return dp[len(coins) - 1][amount]

sln = Solution()
print(sln.change(4, [1,2,3]))
print(sln.change(5, [1,2,5]))

        
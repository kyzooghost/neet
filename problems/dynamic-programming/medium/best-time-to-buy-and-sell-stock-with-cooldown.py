class Solution_AfterNeet(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1: return 0
        # (i, isEmpty) -> max
        dp = {}

        def dfs(i, isBuy):
            if i >= len(prices): return 0
            if (i, isBuy) in dp: return dp[(i, isBuy)]

            cooldown = dfs(i + 1, isBuy)
            if isBuy:
                transact = dfs(i + 1, not isBuy) - prices[i]
            else:
                transact = dfs(i + 2, not isBuy) + prices[i]
            dp[(i, isBuy)] = max(cooldown, transact)
            return dp[(i, isBuy)]

        return dfs(0, True)




# How is this a DP problem hmm....
# In fact how is this a 2D DP problem?
# The original stock problem was two pointer problem - with two pointers on top of each other
# But original stock - was just buy and sell once
# Alright...let's draw this out as a decision tree and see if we can cache it

# Hmm...another perspective is if we use the initial problem as a subproblem
# Yea this problem is pretty hard
# Had to see the Leetcode discussion hint, and take 1 hour 10 mins to get a successful submission
# 85% runtime, 93% memory
# DP of states and state transitions...haven't come across this before zzz
# Both initial approaches I was looking at - backtracking and making initial problem as subproblem - coudn't find a solution
# 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1: return 0

        hold_num = prices[0]
        hold_state = 0
        cooldown_state = 0
        ready_to_buy_state = 0

        # hold_state + sell -> cooldown_state

        # hold_state + wait -> hold_state
        # ready_to_buy_state + buy -> hold_state

        # cooldown_state + wait -> ready_to_buy_state
        # ready_to_buy_state + wait -> ready_to_buy_state
        resp = 0
        for i in range(1, len(prices)):
            cur_price = prices[i]

            new_cooldown_state = max(hold_state, hold_state + cur_price - hold_num)
            new_ready_to_buy_state = max(cooldown_state, ready_to_buy_state)
            
            if hold_state - hold_num <= ready_to_buy_state - cur_price:
                new_hold_state = ready_to_buy_state
                new_hold_num = cur_price
            else:
                new_hold_state = hold_state
                new_hold_num = hold_num
            
            resp = max(resp, new_cooldown_state, new_hold_state, new_ready_to_buy_state)
            hold_state = new_hold_state
            hold_num = new_hold_num
            cooldown_state = new_cooldown_state
            ready_to_buy_state = new_ready_to_buy_state

        return resp

sln = Solution_AfterNeet()
print(sln.maxProfit([1,2,3,0,2]))
print(sln.maxProfit([1,3,4,0,4]))

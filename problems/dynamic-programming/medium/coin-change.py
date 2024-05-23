from typing import List
from collections import deque
# 1 <= coins.length <= 10
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 1000
# Unlimited amount of each coin...fewest number of coins to make exact target amount
# How can we reduce this to a decision tree?
# Fewest number = largest coin #s

# Ok urghhhhh, tried for 1hr 50mins, couldn't get a working solution
class Solution_V3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dict = {}
        q = deque()
        for coin in coins:
            if amount == coin: return 1 
            elif coin < amount:
                dict[coin] = 1
                q.append(coin)

        cur_depth = 1
        while q:
            for _ in range(len(q)):
                sum = q.popleft()

                for coin in coins:
                    print(dict)
                    new_sum = sum + coin
                    if new_sum > amount:
                        continue
                    elif new_sum == amount:
                        return cur_depth + 1
                    else:
                        new_remainder = amount - new_sum
                        if new_remainder in dict: 
                            print(new_remainder, new_sum, dict[new_remainder])
                            return cur_depth + dict[new_remainder] + 1
                        if new_sum not in dict: dict[new_sum] = cur_depth + 1
                        q.append(new_sum)

            cur_depth += 1

        return -1
# Hmm I think this decision tree approach is flawed mm, it's O(N^N)
# The constraints are not as helpful here as with combination-sum, because the total sum is so much bigger. You cannot consider every combination, unlike for combination sum mm
# Must be a way to use % operator here...using decision tree is not great with the constraints
# There can only be a max of 12 coins hmm...
# What if you sort, then use the % operator moving forward...
# Ok got to 50 minute mark, and looking up online hints, use DP to start from n = 0, and walk up to amount?
# Let's try to get every possible result in 1 step, then 2 step, then 3 step...
# Now get memory limited exceeded here haha
class Solution_V2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        q = deque()

        for coin in coins:
            # Quick out
            if amount == coin:
                return 1 
            q.append(coin)
        cur_depth = 1
        while q:
            for _ in range(len(q)):
                sum = q.popleft()
                for coin in coins:
                    new_sum = sum + coin
                    if new_sum > amount:
                        continue
                    elif new_sum == amount:
                        return cur_depth + 1
                    else:
                        q.append(new_sum)

            cur_depth += 1

        return -1

# First things - i.) Any number in coins > amount is ineligible, ii.) Any number in coins can be reached in one step
# I also think we are not going to solve this in better than O(N lg N), so let's sort
# Mmm optimised it a bit with sort but still getting TLE at 39/189 cases
class Solution_V1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        coins.sort()
        self.resp = -1
        self.min_depth = float("inf")

        def dfs(coin_index, depth, running_sum):
            # Base case - past running_sum
            if running_sum > amount:
                return
            # Base case - exceeded min_depth found
            if depth >= self.min_depth:
                return
            # Found match
            if running_sum == amount:
                self.min_depth = depth
                self.resp = self.min_depth
                return
            # Recurse into every other coin
            for i in range(coin_index, -1, -1):
                dfs(i, depth + 1, running_sum + coins[i])

        for i in range(len(coins) - 1, -1, -1):
            if coins[i] <= amount:
                dfs(i, 1, coins[i])

        return self.resp

# Here is a brute force O(N^N) solution, done in 15 minutes
# As expected, TLE mmm, on only 15/189 cases done
# So how can we memoize this, where are the repeated subtrees?
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        self.resp = -1
        self.min_depth = float("inf")

        def dfs(coin_index, depth, running_sum):
            # Base case - past running_sum
            if running_sum > amount:
                return
            # Base case - exceeded min_depth found
            if depth >= self.min_depth:
                return
            # Found match
            if running_sum == amount:
                self.min_depth = depth
                self.resp = self.min_depth
                return
            # Recurse into every other coin
            for i in range(len(coins)):
                dfs(i, depth + 1, running_sum + coins[i])
            
        for i in range(len(coins)):
            dfs(i, 1, coins[i])

        return self.resp

sln = Solution_V3()
# print(sln.coinChange([1,5,10], 12)) #3
# print(sln.coinChange([2], 3)) #-1
# print(sln.coinChange([1], 0)) #0
# print(sln.coinChange([1], 1)) #1
print(sln.coinChange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100)) #10



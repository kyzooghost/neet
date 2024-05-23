from typing import List
from collections import deque
# 1 <= coins.length <= 10
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 1000
# Unlimited amount of each coin...fewest number of coins to make exact target amount
# How can we reduce this to a decision tree?
# Fewest number = largest coin #s

# 60% runtime, 73% memory
# Yep using array vs dict seems to perform much better, even if array contains some sentinel values where dict does not have values
class Solution_AfterNeetIterativeDP_V2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            # Iterate through all coins
            for coin in coins:
                remainder = i - coin
                if remainder >= 0:
                    dp[i] = min(dp[i], 1 + dp[remainder])

        return dp[amount] if dp[amount] != amount + 1 else -1

class Solution_Neet:
    # Wait why does this get 73% runtime, 73% memory even though time + space complexity is the same as what I implemented? Is it because of using an array?
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


# Ok this works, but idk DP is still easier to reason about and implement
# Got TLE with top-bottom recursive on Leetcode anyway lol
class Solution_AfterNeetRecursiveMemoization:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        self.dict = {}

        def dfs(remainder, depth):
            if remainder < 0:
                return None
            if remainder == 0:
                return depth
            if remainder in self.dict:
                return depth + self.dict[remainder]

            min_depth = float("inf")
            for coin in coins:
                dfs_depth = dfs(remainder - coin, depth + 1)
                if dfs_depth: min_depth = min(min_depth, dfs_depth)

            if min_depth == float("inf"): 
                return None
            else:
                self.dict[remainder] = min_depth - depth
                return min_depth

        dfs(amount, 0)
        return self.dict.get(amount, -1)

# Ok watched Neet video, still feel meh about this solution - O(amount) Space and O(len(coins) * amount) time
# Urgh finally accepted, it just feels really weird because it's still an O(len(coins) * amount) time efficiency solution
# But yea greedy doesn't work, and backtracking is O(N^N), so what are you left with?
# You could probably do this in O(1) space, but the bookkeeping would become much more complex
# 5% runtime, 21% memory
class Solution_AfterNeetIterativeDP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dict = { 0 : 0 }

        for i in range(1, amount + 1):
            # Iterate through all coins
            for coin in coins:
                remainder = i - coin
                if remainder < 0: continue
                elif remainder == 0: dict[coin] = 1
                else:
                    if remainder in dict:
                        dict[i] = min(dict[remainder] + 1, dict.get(i, float("inf")))
                    else:
                        continue

        return dict.get(amount, -1)

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

sln = Solution_AfterNeetRecursiveMemoization()
print(sln.coinChange([1,5,10], 12)) #3
print(sln.coinChange([2], 3)) #-1
print(sln.coinChange([1], 0)) #0
print(sln.coinChange([1], 1)) #1
print(sln.coinChange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100)) #10


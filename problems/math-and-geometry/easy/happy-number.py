
# Yay got a working solution for Leetcode in 9 minutes, but 17% runtime and 10% memory lol
class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()

        # Return (new_n, sum)
        def step(n: int) -> int:
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n = n // 10
            return sum
        
        while n != 1:
            n = step(n)
            print(n)
            if n in sum_set: return False
            sum_set.add(n)
        
        return True

sln = Solution()
print(sln.isHappy(19))
print(sln.isHappy(2))
print(sln.isHappy(101))
print(sln.isHappy(100))



# Guaranteed to have a unique solution
# Eih got a successful submission to Neet in 33 minutes, failed on 39/40th test case of Leetcode...very close, just need to address an edge case
# Ok 39% runtime, 10% memory, glad that I got it, but still took an hour zzz. Lol addressing the edge case was just converting < to <=, and people in Leetcode dicussion are complaining about this test case. So we can count this as done in 30 minutes.
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        collate = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(collate) < 0: return -1
        
        l_sum = [0 for i in range(len(gas))]
        l_sum[0] = collate[0]
        min_i = 0
        min_l_sum = l_sum[0]
        for i in range(1, len(gas)):
            l_sum[i] = l_sum[i - 1] + collate[i]
            if l_sum[i] <= min_l_sum:
                min_i = i
                min_l_sum = l_sum[i]

        if min_i == len(gas) - 1:
            return 0
        else:
            return min_i + 1

sln = Solution()
print(sln.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

# Can only be a positive collate value - won't be min value...
# Can overcome min value on the path - find min_value pt - 
# On R - 
# On L - take as is
# l_sum 
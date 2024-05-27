# 48% runtime, 78% memory
# Yep...haven't used a monotonic stack before. Two things about it are weird to me
    # 1.) You discard values from the original array, to maintain the monotonicity
    # 2.) To find the next greatest element, you use a monotonically decreasing stack
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i, t))

            # Found NGE if t > stack_top
            while stack and stack[-1][1] < t:
                popped_node = stack.pop()
                temperatures[popped_node[0]] = i - popped_node[0]
            stack.append((i, t))

        while stack:
            popped_node = stack.pop()
            temperatures[popped_node[0]] = 0
        return temperatures

sln = Solution()
print(sln.dailyTemperatures([73,74,75,71,69,72,76,73]))



# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
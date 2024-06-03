# Ahh don't need two stacks, just need to track max height from L and max height from R
# min(L, R) - height[i]
# Eih the two pointer solution just doesn't sink in as easily as using two monotonically increasing stacks
class Solution_Neet(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pass

# I was thinking of solving this with two monotonically increasing stacks, one from the left and one from the right
# Encounter NGE -> become new height, encounter not NGE -> trap rain water
# 61% runtime, 86% memory
# Sweet did this without much issue, first idea worked and just had one failed submission where I didn't account for the 'middle' trapped section
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_stack, r_stack = [], []
        l_collected, r_collected = 0, 0
        resp = 0
        for i in range(len(height)):
            r_index = len(height) - i - 1
            if not l_stack: l_stack.append(height[i])
            if not r_stack: r_stack.append(height[r_index])

            # Left: If not NGE or same height -> trap rain water
            if height[i] < l_stack[-1]:
                l_collected += l_stack[-1] - height[i]
            else:
                resp += l_collected
                l_collected = 0
                l_stack.append(height[i])

            # Right: If not NGE -> trap rain water
            if height[r_index] <= r_stack[-1]:
                r_collected += r_stack[-1] - height[r_index]
            else:
                resp += r_collected
                r_collected = 0
                r_stack.append(height[r_index])

        return resp
    
sln = Solution()
print(sln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sln.trap([4,2,0,3,2,5]))
print(sln.trap([0,2,0,3,1,0,1,3,2,1]))
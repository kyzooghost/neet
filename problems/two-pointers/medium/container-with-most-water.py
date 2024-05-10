# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution(object):
    # 47% runtime, #60 memory
    # Ughhhh so annoying, felt like I was close but went down the wrong rabbit hole
    # It's so annoying that the solution is simpler than what I was considering too
    # Yes the two pointers start at each side, but how to update the pointers and why that update algorithm works escapes me
    # So start with max-width, try to increase the lowest height you have (at cost of -1 width)

    # Start with max-width, trying to optimize (r - l) * min(height[r], height[l])
    # If we use two pointers and start at either end, you must reduce (r - l) by 1 to explore the next option
    # So we can either move 'l' or 'r'. The area is bounded by the smaller of the two heights.
        # If we move the larger of the two heights, and get a higher height, then we will still be bounded by the smaller height and will be guaranteed to have a smaller area
        # If we move the smaller of the two heights, and get a higher height, then we will have a higher minimum height and hence this is the only way forward
        # Also the smaller height has the maximum area possible for this length, and we know all checked pointers have passed this 'maximum area possible' check
    def maxArea_v1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # If you use two pointers, should be able to do this in O(N) time, but how?
        length = len(height)
        l, r = 0, length - 1
        resp = 0
    
        while l < r:
            area = (r - l) * min(height[r], height[l])
            resp = max(area, resp)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
            
        return resp
 

    # Designed and implemented O(N^2) solution in 11 minutes, but not good enough
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # O(N^2) solution to iterate through each combination - do you have to iterate through each combination?
        # Can't sort here
        # amount of water = min(height) * length
        # There is a max height, and max length - and you cannot excceed this
        resp = 0
        length = len(height)
        l = 0

        while l < length - 1:
            r = l + 1

            while r < length:
                area = (r - l) * min(height[l], height[r])
                resp = max(area, resp)
                r += 1

            l += 1

        return resp

solution = Solution()
# print(solution.maxArea_v1([1,8,6,2,5,4,8,3,7]))
# print(solution.maxArea_v1([1,1]))
# print(solution.maxArea_v1([2,3,4,5,18,17,6]))
print(solution.maxArea([1,8,100,2,100,4,99,8,3,7]))


# Sort is N log N
# Keep trying until impossible to beat?
# Product of all but self?

# resp = (r - l) * min(height[l], height[r])

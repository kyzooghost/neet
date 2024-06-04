# Lol intentionally went into this problem because I was looking at onsites.fyi
# Worked out this question pretty smoothly, probably <20 minutes with an O(N) time and O(N) space solution
# Definitely think the code can be cleaner but can't be bothered at this time at night
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        push_i = 0
        popped_set = set()
        for i in range(0, len(popped)):
            if popped[i] in popped_set: return False

            if not stack:
                if push_i == len(pushed):
                    return False
                else:
                    stack.append(pushed[push_i])
                    push_i += 1
            
            while stack[-1] != popped[i] and push_i < len(pushed):
                stack.append(pushed[push_i])
                push_i += 1

            if push_i == len(pushed) and stack[-1] != popped[i]:
                return False

            # Happy case - we can pop
            popped_set.add(stack.pop())

        return True
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is # valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    # Ok good, done in <10 minutes
    # 89% runtime, 26% memory
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            # Push onto stack
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == ")":
                if stack.pop() != "(":
                    return False
            elif char == "]":
                if stack.pop() != "[":
                    return False
            elif char == "}":
                if stack.pop() != "{":
                    return False
        
        if len(stack) != 0:
            return False
    
        return True

    # 89% runtime, 26% memory
    def isValid_Neet(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {}
        dict['}'] = '{'
        dict[']'] = '['
        dict[')'] = '('

        for char in s:
            # Not closing character
            if char not in dict:
                stack.append(char)
            # Closing character and nothing in stack
            elif len(stack) == 0:
                return False
            elif stack.pop() != dict[char]:
                return False

        if len(stack) != 0:
            return False
    
        return True


solution = Solution()
print(solution.isValid_Neet("()"))
print(solution.isValid_Neet("()[]{}"))
print(solution.isValid_Neet("(]"))
print(solution.isValid_Neet(""))
print(solution.isValid_Neet("[[(())]]"))




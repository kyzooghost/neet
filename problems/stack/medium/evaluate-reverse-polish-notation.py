import math

# Urgh really hate this question
# The concept is really straightforward, but urgh fucking making Python behave with the 'truncate towards zero' requirement. And Leetcode Python is acting differently from local Python or Neetcode python...
# Zzzzzzzzzzzzzzzzzzzzzz so frustrated with myself here, it's a straightforward stack question but implementation of / operator truncating towards 0 in Python zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
# I also had the wrong idea with resp = None at first
# `a//b` will round down with negative number, int(a/b) will round down towards zero
# Also got messed up on order of '/' and '-' operator with the stack
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "/" or token == "*":
                a = stack.pop() # top of stack
                b = stack.pop() # further back
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                else:
                    quotient = float(b) / float(a)
                    stack.append(int(quotient))
            # Else is string representation of number
            else:
                stack.append(int(token))
        return stack.pop()

sln = Solution()
# print(sln.evalRPN(["2","1","+","3","*"]))
# print(sln.evalRPN(["4","13","5","/","+"]))
print(sln.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(sln.evalRPN(["1","2","+","3","*","4","-"]))
# print(sln.evalRPN(["3","11","5","+","-"]))
# print(sln.evalRPN(["4","-2","/","2","-3","-","-"]))
# print(sln.evalRPN())



print(6/-132)
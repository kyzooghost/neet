# Sigh completely styled...I have the right core concept but implementing the carry is gg
# 1.) Need to bitmask in Python to limit to 32-bit #
# 2.) Just while loop of xor and carry. You can deal with multiple carried bits at once...that's new
# 79% runtime, 93% memory
# Well I completely flunked this question, no way I can come up with how to deal with Python binary representation of -1 on the spot
class Solution_AfterNeet(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xffffffff
        if a == 0: return b
        if b == 0: return a
        while b:
            tmp = a
            a = (a ^ b) & MASK
            b = ((tmp & b) << 1) & MASK
        # If MSB is 1 -> is a negative number
        print(a)
        print(a^MASK)

        if a & (1 << 31):
            # Kind of 'double flip' - flip within 32-bit mask, then flip across entire number
            return ~(a^MASK)
        return a
    
# Two's complement - write out positive int, invert digits and +1
# So -n = ~n + 1
# MSB = 1 => Negative number

# Hmm, sum of two integers without using + or -
# So you're forced to use bitwise operation
# Ok this works, but you are still using + operator for i += 1, so disqualified lol
# gg this took 55 minutes because I got really stuck on how to compute the carry
# Also doesn't work for -1 in Python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        resp, carry = 0,0

        i = 0
        while a or b:
            print("hi")
            # Take LSB of a and b
            a_lsb = a & 1
            b_lsb = b & 1
            
            cur_bit = a_lsb ^ b_lsb ^ carry
            # if a_lsb & b_lsb == 1, definitely have a carry
            if a_lsb & b_lsb == 1:
                carry = 1
            else:
                carry = (a_lsb | b_lsb) & carry
            
            # Set current bit for resp
            resp |= (cur_bit << i)

            # Rightshift both a and b
            a >>= 1
            b >>= 1
            i += 1

        resp |= (carry << i)

        return resp

sln = Solution_AfterNeet()
# print(sln.getSum(2, 3))
# print(sln.getSum(1, 1))
# print(sln.getSum(-1, 1))
print(sln.getSum(-1, -3))

# print(sln.getSum(10, 3))
# print(sln.getSum(100, 200))

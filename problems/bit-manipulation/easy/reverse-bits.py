class Solution_V2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Can also 'feed' n into resp
        resp = 0
        
        for _ in range(32):
            cur_bit = n & 1
            resp <<= 1
            resp |= cur_bit
            n >>= 1

        return resp

# "n" is an integer
# 87% runtime, 66% memory
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        resp = 0
        for i in range(32):
            # Check if bit set
            if (1 << i) & n != 0:
                # Set reverse bit on resp
                resp |= (1 << (31 - i))
        return resp

sln = Solution_V2()
# print(sln.reverseBits(43261596))
print(sln.reverseBits(50))

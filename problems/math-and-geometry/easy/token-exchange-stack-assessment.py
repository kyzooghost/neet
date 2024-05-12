# Let us consider an infinite sequence of stacks indexed from 0, and an
# exchange operation that removes two tokens from a stack and adds one
# token to the next stack.

# For example, lets assume there are two tokens on stack 0 and three on
# stack 1. Two tokens from stack 0 may be exchanged for one new token
# on stack 1. After that operation, there are four tokens on stack 1 that
# may be exchanged for two new tokens on stack 2. Finally, a new token
# may be added to stack 3 by exchanging two tokens from stack 2. This
# gives us: stacks 0, 1 and 2 empty, and stack 3 with one token.
# Given the heights of the first N stacks, find the minimum number of
# tokens that may remain after any number of exchange operations. You
# may assume that all of the tokens are identical. All uninitialized stacks
# are empty by default.

# Write a function: def solution (A)
# that, given an array A of N integers, representing the heights of the first N stacks in the sequence, returns the minimum number of tokens which may remain on the stacks after any number of exchange operations. Examples:

# 1. Given A = [2, 3], the function should return 1, as explained above. 

# 2. Given A = [1, 0, 4, 1], the function should return 3. One token from stack 0 cannot be exchanged. Then the four tokens from stack 2 can be exchanged for two tokens on stack 3. In the end, two of the three tokens from stack 3 can be exchanged for one token on stack 4. That gives us three tokens, one on each of the stacks 0, 3 and 4.


# 3. Given A = [5], the function should return 2. Four of the five tokens from stack 0 can be exchanged for two on stack 1, and then in turn for one token on stack 2. After that we have one token on each of stacks 0 and

# 4. Given A = [4, 0, 3, 0], the function should return 1. The four tokens from stack 0 can be exchanged for two on stack 1, then for one token on stack 2. The four tokens that are now on stack 2 can be exchanged for two on stack 3, then for one token on stack 4.

# Write an efficient algorithm for the following assumptions:
# - N is an integer within the range [1..100,000];
# - each element of array A is an integer within the range [0..1,000,000].

def solution(A):
    resp = 0

    # Blocks exchanged from last stack
    exchanged_blocks = -1
    length = len(A)
    i = 0

    # Break if i.) No more stacks in A and ii.) No more blocks exchanged from last stack
    # O(N) time efficiency, O(1) space efficiency
    while i < length or exchanged_blocks > 0:
        # Initialize `exchanged_blocks` for first loop - we are guaranteed at least one stack
        if i == 0:
            exchanged_blocks = 0

        # Take blocks exchanged from last pass
        blocks_after_exchange = exchanged_blocks // 2

        # If we are in still in A, add blocks from A
        if i < length:
            blocks_after_exchange += A[i]
        
        # Increment resp by blocks that we cannot exchange
        leftover_blocks = blocks_after_exchange % 2
        resp += leftover_blocks

        # Compute blocks to exchange in next stack
        exchanged_blocks = blocks_after_exchange - leftover_blocks
        i += 1

    return resp

def solution1(A):
    resp = 0

    # Blocks exchanged from last stack
    exchanged_blocks = 0
    length = len(A)

    # Want to iterate for i > N
    for i in range(1000000):
        # Break if no more stacks in A, and no more exchanged blocks
        if (i >= length and exchanged_blocks == 0):
            break

        # Take blocks exchanged from last pass
        blocks_after_exchange = exchanged_blocks // 2

        # If we are in still in A, add blocks from A
        if i < length:
            blocks_after_exchange += A[i]
        
        # Increment resp by blocks that we cannot exchange
        leftover_blocks = blocks_after_exchange % 2
        resp += leftover_blocks

        # Compute blocks to exchange in next stack
        exchanged_blocks = blocks_after_exchange - leftover_blocks

    return resp


print(solution([0, 0, 0, 0, 0]))
print(solution([1000000, 1000000, 1000000, 1000000, 1000000, 1000000]))
print(solution([2, 3]))
print(solution([1, 0, 4, 1]))
print(solution([5]))
print(solution([4, 0, 3, 0]))

print("------")
print(solution1([0, 0, 0, 0, 0]))
print(solution1([1000000, 1000000, 1000000, 1000000, 1000000, 1000000]))
print(solution1([2, 3]))
print(solution1([1, 0, 4, 1]))
print(solution1([5]))
print(solution1([4, 0, 3, 0]))




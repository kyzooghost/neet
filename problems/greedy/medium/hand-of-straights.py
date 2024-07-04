from collections import Counter
from heapq import heappop, heappush

# Let's try using min PQ
# 26% runtime, 34% memory
# Yea more straightforward to use a min PQ here for the 'delete the min' operation
# Trying to hand-implement the 'delete the min' conditionally operation without minPQ or min(Counter) is too hard to do for an interview
class Solution_V3(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        hand_counter = Counter(hand)
        card_pq = []
        for card in hand_counter.keys():
            heappush(card_pq, card)

        while card_pq:
            hand_start = card_pq[0]
            for card in range(hand_start, hand_start + groupSize, 1):
                if card not in hand_counter: return False
                hand_counter[card] -= 1
                if hand_counter[card] == 0:
                    del hand_counter[card]
                    if card_pq[0] == card: heappop(card_pq)
        return True

# 93% runtime, 67% memory
# Yep got O(N lg N) solution, but this was so much trickier to implement than the O(N^2) solution
# I think there must be a much simpler and cleaner way to implement the O(N lg N) solution
# Yea 40 lines of code for a solution == Hard, and this isn't a hard
class Solution_V2(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        # N lg N is still better than N^2 in the dirtier solution
        hand.sort()
        seen_i = set()
        hand_start_i = 0

        # [1,2,2,3,3,4,6,7,8]
        while hand_start_i < len(hand):
            # Start hand
            cur_i = hand_start_i
            # Ensure we can find next hand_start
            hand_start_i = len(hand)

            # Initialize loop with first card
            cur_card = hand[cur_i]
            seen_i.add(cur_i)
            hand_size = 1

            while hand_size < groupSize:
                # Out of bounds
                if cur_i >= len(hand):
                    return False
                if cur_i in seen_i: 
                    cur_i += 1
                    continue
                # Not seen before, but can be next_hand_start
                if hand[cur_i] == cur_card:
                    if cur_i not in seen_i: hand_start_i = min(cur_i, hand_start_i)
                    cur_i += 1
                    continue
                # Not a straight
                if hand[cur_i] != cur_card + 1:
                    return False
                # Happy path - straight
                seen_i.add(cur_i)
                cur_card = hand[cur_i]
                cur_i += 1
                hand_size += 1
            
            hand_start_i = min(cur_i, hand_start_i)

        return True

# Straights
# Well I went for the dirty solution because I was getting stuck in the cleaner solution I wanted to achieve
# Ok - so got first submission in 17 minutes, 20% runtime, 63% memory
# Feels bad - O(N) space, O(N)
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0: return False

        # O(N) time
        hand_counter = Counter(hand)

        while len(hand_counter) > 0:
            # O(N^2 // groupSize) - this line is the bottleneck
            hand_start = min(hand_counter.keys())
            # O(N) time total for this loop
            for i in range(hand_start, hand_start + groupSize, 1):
                if i not in hand_counter: return False
                hand_counter[i] -= 1
                if hand_counter[i] == 0: del hand_counter[i]

        return True

sln = Solution_V3()
print(sln.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)) # True
print(sln.isNStraightHand([1,2,3,6,2,3,4,7,9], 3)) # False
print(sln.isNStraightHand([1,2,4,2,3,5,3,4], 4)) # True
print(sln.isNStraightHand([1,2,3,3,4,5,6,7], 4)) # False

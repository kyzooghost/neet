from collections import Counter

# 73% runtime, 83% memory
# I guess using Counter is not bad
class Solution_V3(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0: return False
        # O(N) space and O(N) time
        card_count = Counter(hand)
        # O(N lg N) worst case
        sorted_cards = sorted(card_count.keys())

        # Worst case O(2N)
        for card in sorted_cards:
            if card_count[card] > 0:
                count = card_count[card]
                for i in range(groupSize):
                    if card_count[card + i] < count:
                        return False
                    card_count[card + i] -= count

        return True
        

# Hmm I just need the minimum each time
# So could use O(N) space for the frequency dict, O(N * len(hand) // groupSize) time
# No need to sort here, just find the min each time
# 16% runtime, 83% memory
# Hmm actually, we should be able to get all the group starts in a single pass through the dict
# Well I read several solutions, there is no O(N) solution like I was aiming for. 
class Solution_V2(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0: return False
        # O(N) space and O(N) time
        dict = {}
        for num in hand:
            dict[num] = dict.get(num, 0) + 1

        while dict:
            # Find a group start
            group_start = None
            for key in dict.keys():
                if key - 1 not in dict:
                    group_start = key
                    break
            # Remove group from dict
            for i in range(groupSize):
                cur = group_start + i
                if cur not in dict:
                    return False
                else:
                    dict[cur] -= 1
                    if dict[cur] == 0: del dict[cur]
        return True



# This works, but horribly time and space inefficient - 5% runtime, 14% memory with the sort
# hand.sort() actually does nothing here, but even without sort - 5% runtime and 34% memory hmm
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0: return False

        # N space
        dict = {}
        for num in hand:
            dict[num] = dict.get(num, 0) + 1

        # Find each group
        for _ in range(int(len(hand) / groupSize)):
            group_start = min(list(dict.keys()))
            for i in range(groupSize):
                cur = group_start + i
                if cur not in dict:
                    return False
                else:
                    dict[cur] -= 1
                    if dict[cur] == 0: del dict[cur]
        
        return True

        # Find smallest num, create and remove set, start again
        

        
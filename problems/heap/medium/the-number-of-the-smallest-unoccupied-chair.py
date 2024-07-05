# Process events by time - time, friend #
# Keep track of lowest chair available
# (time, friend_i, event)
# Keep track of friend -> chair
# Keep track of lowestChair

# Did this fried at midnight so didn't time myself
# 80% runtime, 60% memory
# Failed first submission, fixed one edge case which wasn't hard to find - should have been able to find it if I wrote out the test case
# Got 2nd submission
# So O(N lg N) time to sort into heap, O(N) space
from heap import heappush, heappop

# Hmm another solution is to use another pq to store the empty seats
class Solution_V2(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        empty_chairs = list(range(0, len(times)))
        friend_to_seat = [-1 for _ in range(len(times))]

        pq = []
        for n in range(len(times)):
            # (time, friend_n)
            # event - True if sit, False if stand
            # But end < start
            start, end = times[n][0], times[n][1]
            heappush(pq, ((start * 2) + 1, n))
            heappush(pq, (end * 2, n))

        while pq:
            time, friend_n = heappop(pq)
            # Is sit
            if time % 2 == 1:
                if friend_n == targetFriend: return empty_chairs[0]
                friend_to_seat[friend_n] = heappop(empty_chairs)
            # Is leave
            else:
                heappush(empty_chairs, friend_to_seat[friend_n])

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        pq = []
        for n in range(len(times)):
            # (time, friend_n)
            # event - True if sit, False if stand
            # But end < start
            start, end = times[n][0], times[n][1]
            heappush(pq, ((start * 2) + 1, n))
            heappush(pq, (end * 2, n))

        lowestChair = 0
        friend_to_chair = {}
        chair_to_friend = {}

        while pq:
            time, friend_n = heappop(pq)
            # Is sit
            if time % 2 == 1:
                if friend_n == targetFriend: return lowestChair
                friend_to_chair[friend_n] = lowestChair
                chair_to_friend[lowestChair] = friend_n
                while lowestChair in chair_to_friend:
                    lowestChair += 1
            # Is leave
            else:
                chair = friend_to_chair[friend_n]
                del friend_to_chair[friend_n]
                del chair_to_friend[chair]
                if chair < lowestChair: lowestChair = chair
        
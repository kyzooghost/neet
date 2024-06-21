# n cooling time between each task
# How could you use a heap here?
# Store last turn on heap - know what can be redone
# Choose from first on heap, if nothing eligible, then must idle
# At all turns - want the largest count that can be used
from heapq import heappush, heappop
from collections import defaultdict, deque

# 54% runtime, 65% memory
# Dang this took me an hour to get my first successful submission
# The problem of 'how to find the biggest count letter that is eligible this cycle' needed two data structures gg - a priority queue and a normal queue
class Solution_V3(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        # (neg_count, task)
        eligible_heap = []
        for task in task_count.keys():
            heappush(eligible_heap, (-task_count[task]))
        resp = 0
        # (next_turn, count, task)
        ineligible_queue = deque()

        while eligible_heap or ineligible_queue:
            resp += 1
            if ineligible_queue and ineligible_queue[0][0] <= resp:
                (next_turn, neg_count) = ineligible_queue.popleft()
                heappush(eligible_heap, (neg_count))
            
            if eligible_heap:
                neg_count = heappop(eligible_heap)
                if neg_count < -1: ineligible_queue.append((resp + n + 1, neg_count + 1))
        return resp

# Well works but TLE on 55/71 cases
class Solution_V2(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        # (count, next_usable_turn, letter)
        task_heap = []
        for task in task_count.keys():
            heappush(task_heap, (-task_count[task], -1, task))
        resp = 0

        # Need to know - biggest count task that is eligible
        # Loop through entire heap on each turn?

        while task_heap:
            resp += 1
            tmp_stack = []
            # Iterate through heap until find eligible task
            while task_heap:
                (neg_count, next_usable_turn, task) = heappop(task_heap)
                if next_usable_turn < resp:
                    if neg_count < -1: heappush(task_heap, (neg_count + 1, resp + n, task))
                    break
                else:
                    tmp_stack.append((neg_count, next_usable_turn, task))
            
            while tmp_stack: heappush(task_heap, tmp_stack.pop())

        return resp

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        # (count, next_usable_turn, letter)
        task_heap = []
        for task in task_count.keys():
            heappush(task_heap, (-task_count[task], task_count[task], task))
        resp = 0

# Need to know - biggest count task that is eligible
# Loop through entire heap on each turn?

        while task_heap:
            resp += 1
            (next_usable_turn, count, task) = task_heap[0]
            print(task_heap)
            # print(next_usable_turn, count, task)
            # Can pop
            if next_usable_turn < resp:
                heappop(task_heap)
                if count > 1:
                    heappush(task_heap, (resp + n, count - 1, task))

        return resp
    

# One PQ -> largest count at any time
# What to do if its not eligible?
# Keep eligible and ineligible pool?
# Add back in at eligible time? - use deque to decide

sln = Solution_V3()
print(sln.leastInterval(["A","A","A","B","B","B"], 2)) #8
print(sln.leastInterval(["A","C","A","B","D","B"], 1)) #6
print(sln.leastInterval(["A","B","A"], 2)) #4
print(sln.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 1))



# print(sln.leastInterval())
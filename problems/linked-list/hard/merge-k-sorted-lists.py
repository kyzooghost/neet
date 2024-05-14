# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    # mergeKLists_Neet
    # Ceebs writing it out, but it is using merge-two-sorted-lists.py as a subroutine, and repeatedly merging pairs of linked lists
    # Merge two sorted lists = O(M + N), where M and N is the # of nodes in each list
    # So this approach would be O(K ln N) time, where K = total # of nodes, N = len(list)
    # O(N) extra space - for temp array of list heads

    # 62% runtime, 52% memory
    # Ok the heapq API for Python is kinda nice. To make it a max priority queue, just use negative value damn.
    # O(K ln N) - where K = total # of nodes, N = len(list). O(N) extra space. Easier to implement than Neet solution, given familiarity with heapq API
    def mergeKLists_Heap(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Hmm this should be doable if we can do the merge two-sorted-lists problem
        cur = dummy = ListNode()
        min_pq = []

        # Initialize min_pq
        for list_head in lists:
            if list_head:
                heappush(min_pq, (list_head.val, list_head))

        while len(min_pq) != 0:
            # Get minimum
            min_head = heappop(min_pq)[1]

            # Update cur
            cur.next = min_head
            cur = cur.next

            # Update min_head
            min_head = min_head.next

            # Insert into heap
            if min_head:
                heappush(min_pq, (min_head.val, min_head))

        return dummy.next

    # Sweet did a hard problem in 16 minutes
    # 8% runtime, 73.5% memory
    # Can we improve the time efficiency? Well the subroutine to get the minimum node for each round is O(N), which makes our implemention O(MN) where M = Total # of nodes, N = len(lists)
    # We could maintain a minimum priority queue of node values - this is a space-for-time tradeoff where we get O(lg N) time efficiency for O(N) space
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Hmm this should be doable if we can do the merge two-sorted-lists problem
        cur = dummy = ListNode()

        def is_lists_exhausted():
            for ptr in lists:
                if ptr is not None:
                    return False
            return True
            
        # Stop when each list element is None
        while is_lists_exhausted() == False:
            min_index, min_value = -1, 10 ** 4
            
            # Get minimum val from this round, exclude None
            for i, ptr in enumerate(lists):
                if ptr and ptr.val < min_value:
                    min_value = ptr.val
                    min_index = i
            
            # Update cur
            cur.next = lists[min_index]
            cur = cur.next
            # Update minimum node from this round
            lists[min_index] = lists[min_index].next

        return dummy.next




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# reverse nodes k at a time
# return modified list
# k <= len(list). Remaining nodes - no reversal
# No altering list node values, so just changing pointers basically
# Took me longer to get Neet solution correct because there is at least one more ptr lying around

class Solution_Neet(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: return head
        dummy = ListNode(0, head)
        groupPrevEnd = dummy

        while True:
            groupEnd = groupPrevEnd
            for _ in range(k):
                groupEnd = groupEnd.next
                if not groupEnd: return dummy.next

            nextGroupStart = groupEnd.next

            # reverse group
            prev, ptr = nextGroupStart, groupPrevEnd.next

            while ptr != nextGroupStart:
                tmp = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = tmp
            
            tmp = groupPrevEnd.next
            groupPrevEnd.next = prev
            groupPrevEnd = tmp


# slow, fast ptr - 
# fast ptr goes ahead first -> if fast is null is null we have finished
# tmp ptr, while ptr != fast then reverse

# 82% runtime, 44% memory - got first submission in 45 minutes
# What I learned from coding interview is run through the edge cases yourself first, BEFORE SUBMITTING CODE
# The aim is first submission pass
# But yea zzz this kind of thing is hard, ptr logic is just fragile especially when I have 3 dynamics ptrs running around in my implementation
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1: return head

        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy

        while fast:
            # Update fast to 'last of batch'
            for _ in range(k):
                fast = fast.next
                if not fast: return dummy.next
            
            # Initialize reversal
            tmp = slow.next
            slow.next = fast
            slow = tmp
            tmp = tmp.next
            slow.next = fast.next

            # Reversal loop
            while slow != fast:
                tmp2 = tmp.next
                tmp.next = slow
                slow = tmp
                tmp = tmp2

            # Update pointers back to next set - fast, slow now at the back
            for _ in range(k - 1):
                fast = fast.next
                slow = slow.next

        return dummy.next
        
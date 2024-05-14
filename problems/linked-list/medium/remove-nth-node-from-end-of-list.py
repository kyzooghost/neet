# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    # Try the same with a dummy pointer
    # 91% runtime, 15% memory
    # Hmm basically the same, just using a dummy and for-loop break to account for the n == 1 edge case
    def removeNthFromEnd_Neet(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        slow, fast = dummy, head

        for _ in range(n):
            if fast is None:
                break
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Change links
        slow.next = slow.next.next
        return dummy.next
    
    # Yay got this first try
    # 70% runtime, 46% memory
    # Slow + fast pointer, and single edge case of n == 1
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Initialise slow + fast pointers
        slow, fast = head, head

        for _ in range(n):
            fast = fast.next
        
        # Edge case - we are at first element in linked list, return 2nd element (1st element is implicitly lost)
        if fast is None:
            head = head.next
            return head

        # Move slow and fast pointers, until fast pointer reach end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        # Change links
        tmp1, tmp2 = slow.next, slow.next.next
        slow.next = tmp2
        # We don't actually need to remove this pointer, it can have nothing pointing to it?
        tmp1.next = None

        return head
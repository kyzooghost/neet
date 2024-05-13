# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    # 92% runtime, 20% memory
    # Ok much more streamlined 'find-halfway' algorithm 
    # Set both midway nodes to point to None
    def reorderList_Neet(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # If start fast at head.next -> middle for odd numbers, left-half for even numbers
        # If start fast at head -> middle for odd numbers, right-half for even numbers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Slow is middle (for odd) or left of middle (for even)
        
        # Set middle to None, reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head


    # 74% runtime, 13% memory
    # Ok had the correct idea almost straight away, but I took way too long to implement. Not timed as couldn't sit down for entire time, but having to walk through the two half lists took too long
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if head is None:
            return head
        if head.next is None:
            return head

        # Hmm...can only change next value
        # Need two pointers, one from start, one at end
        # Need to reverse half of the linked list
        dummy = ListNode()
        half, tail  = head, head
        is_half_walk = True

        # Work where the halfway point is
        while tail is not None:
            tail = tail.next
            if is_half_walk and tail is not None:
                half = half.next
            is_half_walk = False if is_half_walk else True

        # Reverse list from half
        prev_half = None

        while half is not None:
            # Set local next
            next_half = half.next
            # Reverse pointer
            half.next = prev_half
            # Update prev
            prev_half = half
            # Update half
            half = next_half

        # Walk through left half, and reversed right half
        cur = dummy
        while prev_half is not None and head is not None:
            # Move to left half
            cur.next = head
            cur = cur.next
            head = head.next

            if head is None and prev_half.next is None:
                break

            # Move to reverse right half
            cur.next = prev_half
            cur = cur.next
            prev_half = prev_half.next

        return dummy.next
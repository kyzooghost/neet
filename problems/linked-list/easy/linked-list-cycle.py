# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 51% runtime, 26% memory
    # Lol, didn't know you can just do a strict equality check for two objects in Python like this
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False     

    # 80% runtime, 97% memory
    # Slow + fast pointer does not work here, because how can you know that the pointers are at the same node
    # Instead just use single pointer starting from dummy node, then change value to 'visited' marker as you traverse
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur:
            if cur.val is None:
                return True
            cur.val = None
            cur = cur.next

        return False
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Find out length of each LL
# Pad out shorter LL...
# Which digits line up?
# Iterate to the other end, and pad out the shorter LL

# Ok got 43% runtime, 91% memory
# But I took 17 minutes, I got tripped up by this one tbh. If I had it straight in my head I would have done it in less than 10 minutes
# Tripped up by whether I needed to return the sum in reverse order or not
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        new_root = ListNode()
        ptr = new_root

        carry = 0
        while p1 or p2:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0

            sum = (p1_val + p2_val + carry)
            ptr.val = sum % 10
            carry = 1 if sum >= 10 else 0

            if p1: p1 = p1.next
            if p2: p2 = p2.next

            if p1 or p2:
                ptr.next = ListNode()
                ptr = ptr.next
        
        if carry == 1:
            ptr.next = ListNode(1)

        return new_root
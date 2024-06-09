"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Just need a way of being able to hash a node
# Ok got it within 19 minutes, 35% runtime, 37% memory
# Failed first submission because didn't account for head == None edge case
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        resp = Node(head.val)
        ptr, ptr_new = head, resp

        # old node => new node
        old_to_new = {}
        old_to_new[head] = resp

        # Populate next
        while ptr.next:
            # Create new node
            new_node = Node(ptr.next.val)

            # Set next
            ptr_new.next = new_node

            # Update dict
            old_to_new[ptr.next] = ptr_new.next

            # Update ptrs
            ptr = ptr.next
            ptr_new = ptr_new.next

        # Populate random - should be no new nodes created
        ptr, ptr_new = head, resp
        while ptr:
            if ptr.random:
                ptr_new.random = old_to_new[ptr.random]
            ptr = ptr.next
            ptr_new = ptr_new.next

        return resp

        
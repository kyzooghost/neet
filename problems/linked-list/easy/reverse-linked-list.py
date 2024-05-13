# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __init__(self, vals):
        """
        :type head: List[int]
        """
        if len(vals) == 0:
            self.val = None
            self.next = None
        else:
            self.val = vals[0]
            pointer = self
            for i in range(1, len(vals)):
                pointer.next = ListNode(vals[i])
                pointer = pointer.next

class Solution(object):

    def reverseList_InPlace(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # [1, 2]

        if head is None:
            return head

        # 1
        # 2
        # None
        # 2 -> 1
        # 

        # Iterate to tail
        while head.next is not None:

            # Pointer to last head
            last_head = head

            # Pointer to current head
            head = head.next

            # Pointer to next head, can be None
            next_head = head.next

            # Change current head pointer
            head.next = last_head

            # If no next head, we are at tail -> stop
            if (next_head == None):
                return head
            # Else go to next head
            else:
                head = head.next

    # 7% runtime, 13% memory
    # Feel like I took way too long to do an easy, close to 30 minutes
    # Feel like I am very clumsy with interacting with a LinkedList in Python, so need more study and practice here
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # O(N) - Iterate through entire linked list and get List of vals
        # Then create new LinkedList, but unfamiliar with LinkedList API

        if head is None:
            return head
        if head.next is None:
            return head
        
        vals = []
        
        # Iterate to tail
        while head.next is not None:
            vals.append(head.val)
            head = head.next

        new_tail = head

        # Head is now the last node, reconstruct the LinkedList
        for i in range(len(vals) -1, -1, -1):
            new_tail.next = ListNode(vals[i])
            new_tail = new_tail.next

        return head

solution = Solution()
print(solution.reverseList([1,2,3,4,5]))
print(solution.reverseList([]))


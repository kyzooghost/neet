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

    # 20% runtime, 18% memory
    # This is my favourite - just two parameters for recursive call, but 1 temporary parameter for next inside
    def reverseList_InPlaceRecursiveV2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse(prev, cur):
            if cur is None:
                return prev
            else:
                next_node = cur.next
                cur.next = prev
                return reverse(cur, next_node)
        
        return reverse(None, head)

    # 16% runtime, 94% memory
    def reverseList_Neet(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        
        prev_node = None

        while head is not None:
            next_node = head.next
            # Reverse pointer
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node

    # 45% runtime, 48% memory
    # Hmm, also ok to return prev, but still weird edge cases on head and tail
    def reverseList_InPlaceV2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        
        prev_node, next_node = None, head

        while head is not None:
            next_node = head.next
            # Reverse pointer
            head.next = prev_node
            prev_node = head
            head = next_node

        if head is None:
            return prev_node
        else:
            return head


    # 65% runtime, 6% memory
    # Hahahaha recursive was much easier to reason through, but is more memory intensive
    # Python doesn't support tail call recursion mm
    # Should probably start with the recursive case first - easiest to implement
    def reverseList_InPlaceRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        def reverse(prev_node, current_node, next_node):
            # Reverse pointer
            current_node.next = prev_node

            if next_node == None:
                return current_node
            else:
                return reverse(current_node, next_node, next_node.next)

        return reverse(None, head, head.next)

    # 86% runtime, 77% memory
    # Urghhhh...this took way too long to work out for an easy, maybe up to 2 hrs
    # Key points
    #   Edge case - None, Single LinkedNode
    #   What happens to the original head in happy case - .next becomes None
    #   What happens to the original tail in happy case - .next was None, becomes something
    #   When we do stop - When next_node becomes None
    #   How many pointers? - 3, prev + current + next
    def reverseList_InPlace(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        
        prev_node, next_node = head, head.next
        head.next = None

        while next_node is not None:
            # Change current pointer
            head = next_node

            # Update next pointer
            next_node = head.next

            # Reverse current pointer
            head.next = prev_node

            # Update prev_node
            prev_node = head

        return head
    
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


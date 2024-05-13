# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    ## 77% runtime, 91% memory
    # Ok can use dummy_head instead of choosing which head to start at
    # Also if either list is exhausted, just append remainder of other list
    def mergeTwoLists_Neet(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy_head = ListNode()
        cur = dummy_head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1 is None:
            cur.next = list2
        elif list2 is None:
            cur.next = list1

        return dummy_head.next        

    # Yay did it first go in ~17 minutes - 10 minutes coding and 7 minutes manually running through the test case
    # 67% runtime, 8% memory
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Edge cases where either list doesn't exist
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Choose smallest head, putting cur pointer at it
        head, cur = None, None
        if list1.val < list2.val:
            head, cur = list1, list1
            list1 = list1.next
        else:
            head, cur = list2, list2
            list2 = list2.next

        # Stop loop when both Linked Lists have been traversed
        while list1 is not None or list2 is not None:
            # list1 exhausted
            if list1 is None:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
            # list2 exhausted
            elif list2 is None:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            # Both lists exist, do comparison
            else:
                # Walk to next in list1
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                # Walk to next in list2
                else:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next

        return head    
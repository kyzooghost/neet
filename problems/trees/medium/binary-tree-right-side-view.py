from collections import deque

# Inorder: Left -> Root -> Right...Give BST in order
# Preorder - Root -> Left -> Right...Create copy of a tree. Put nodes in preorder, then insert in this order (for BST?)
# Postorder - Left -> Right -> Root...Delete tree from leaf to root

# 44% runtime, 84% memory
class Solution_v2(object):
    # If literally rightmost node at each level - use BFS, append the last val encountered
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        resp = []
        if not root: return resp
        queue = deque([root])
        while queue:
            queue_len = len(queue)
            i = 0
            while i < queue_len - 1:
                ptr = queue.popleft()
                if ptr.left: queue.append(ptr.left)
                if ptr.right: queue.append(ptr.right)
                i += 1

            ptr = queue.popleft()
            if ptr.left: queue.append(ptr.left)
            if ptr.right: queue.append(ptr.right)
            resp.append(ptr.val)

        return resp

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Got first successful submission in <10 minutes - 13% runtime, 20% memory
# Feels good to get a successful submission for first submission after spending half the day stuck with median-of-two-sorted-arrays yesterday
class Solution(object):
    # If literally rightmost node at each level - use BFS, append the last val encountered
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        resp = []
        if not root: return resp
        queue = deque([root])
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                ptr = queue.popleft()
                if ptr.left: queue.append(ptr.left)
                if ptr.right: queue.append(ptr.right)
                # Append last val encountered for each BFS level
                if i == queue_len - 1:
                    resp.append(ptr.val)

        return resp
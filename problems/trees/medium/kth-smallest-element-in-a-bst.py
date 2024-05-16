# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # 54.5% runtime, 97% memory
    # Lol ok, so you can set the value to a class property, to persist it as a global variable across recursive calls
    def kthSmallest_Recursive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.num = 0
        self.dfs(root, k)
        return self.num

    def dfs(self, node, k):
        if node is None or self.count >= k:
            return
        self.dfs(node.left, k)
        if self.count < k:
            self.count += 1
            self.num = node.val
        self.dfs(node.right, k)

    # Order that elements are popped - inorder
    def kthSmallest_Neet(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

    # 59% runtime, 33% memory
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Inorder traversal with a counter
        ptr, stack, i = root, [], 1

        while ptr or stack:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack.pop()
                if i == k:
                    return ptr.val
                else:
                    i += 1
                ptr = ptr.right
        
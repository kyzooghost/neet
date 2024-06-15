# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We can solve with DFS, we want to find the depth of left subtree and right subtree
# Yea ok, it's easiest to work out DFS algorithm here by working from a leaf node, rather than the root node
# 64% runtime, 24% memory
# Lol Leetcode and Neetcode discussion have a consensus that this is a medium problem
class Solution_V2(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.resp = float("-inf")

        def dfs(ptr):
            if not ptr: return 0
            l = dfs(ptr.left)
            r = dfs(ptr.right)
            self.resp = max(self.resp, l + r)
            return 1 + max(l, r)

        dfs(root)
        return self.resp

# Sigh very frustrated with myself that I tripped up on an easy
# I am definitely overcomplicating the code
# Was looking for a quick pick-me-up but tripped up on this zzzzzzzzzzzzzzzzzzzzzz
# 37% runtime, 10% memory
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.resp = float("-inf")
        def dfs(ptr, depth):
            if not ptr: return depth - 1
            left_subtree_depth = dfs(ptr.left, depth + 1)
            right_subtree_depth = dfs(ptr.right, depth + 1)
            left_path = left_subtree_depth - depth
            right_path = right_subtree_depth - depth
            path_length = left_path + right_path
            self.resp = max(self.resp, path_length)
            return max(left_subtree_depth, right_subtree_depth)

        dfs(root, 0)
        return self.resp
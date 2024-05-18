# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 55% runtime, 12% memory
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0        
        self.resp = float("inf")

        def dfs(node, depth):
            if node is None:
                return
            if not node.left and not node.right:
                self.resp = min(self.resp, depth)
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.resp
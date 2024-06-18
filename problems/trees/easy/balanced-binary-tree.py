# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right  

# Lol didn't even give the definition for 'height-balanced'
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# Well, DFS to find height, compare L and R
# Took 7 minutes, for 48% runtime and 28% memory. Mmm 
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.resp = True

        def dfs(ptr):
            if not ptr: return 0
            l = dfs(ptr.left)
            r = dfs(ptr.right)
            if abs(l - r) > 1: self.resp = False
            return 1 + max(l, r)
        
        dfs(root)
        return self.resp
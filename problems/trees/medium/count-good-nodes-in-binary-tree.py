# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 98% runtime, 49% memory
class Solution_Neet(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(ptr, prev_max):
            if not ptr: return 0
            res = 0
            cur_max = prev_max
            if ptr.val >= prev_max:
                res += 1
                cur_max = ptr.val
            return res + dfs(ptr.left, cur_max) + dfs(ptr.right, cur_max)

        return dfs(root, root.val)
    
# Sweet got first successful submission for a medium in 4 minutes
# 56% runtime, 94% memory
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.resp = 0
        def dfs(ptr, prev_max):
            if not ptr: return
            if ptr.val >= prev_max:
                self.resp += 1
                prev_max = ptr.val
            dfs(ptr.left, prev_max)
            dfs(ptr.right, prev_max)

        dfs(root, float("-inf"))
        return self.resp
        
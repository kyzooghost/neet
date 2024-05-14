# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # Basically the same as my iterative DFS implementation, just slightly different null node treatment
    def maxDepth_Neet3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        stack = [[root, 1]]
        resp = 1
        while stack:
            node, depth = stack.pop()
            if node:
                resp = max(resp, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return resp

    # 79% runtime, 86% memory
    # BFS using queue
    def maxDepth_Neet2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


    # Lmao the one liner solution, different type of recursive implementation though
    # Thinking starts at bottom, rather than root
    # 86% runtime, 86% memory
    def maxDepth_Neet1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth_Neet1(root.left), self.maxDepth_Neet1(root.right))


    # 94% runtime, 98% memory
    def maxDepth_Iterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = []
        stack.append((root, 1))

        resp = 1
        while len(stack) != 0:
            node, node_depth = stack.pop()
            resp = max(resp, node_depth)
            if node.left:
                stack.append((node.left, node_depth + 1))
            if node.right:
                stack.append((node.right, node_depth + 1))

        return resp

    # 62% runtime, 9% memory
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def visit(node, depth):
            l, r = 0, 0
            if node.left:
                l = visit(node.left, depth + 1)
            if node.right:
                r = visit(node.right, depth + 1)
            return max(depth, l, r)
        
        return visit(root, 1)
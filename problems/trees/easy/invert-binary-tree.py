# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def invertTree_NeetIterative(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    # Neet - 10% runtime, 56% memory
    def invertTree_Neet(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        # Swap only need three lines
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree_Neet(root.left)
        self.invertTree_Neet(root.right)
        return root


    # 87% runtime, 86% memory
    def invertTree_Iterative(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            l, r = node.left, node.right
            node.left, node.right = r, l
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    # 99% runtime, 56% memory
    # Ok cool did it in 12 minutes, but haven't done a tree problem in a long time
    # Need to study up on tree traversal implementation
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        # Invert...means put things in the opposite order
        # But we are just switching the left pointer with the right pointer no?

        def invert(node):
            if node is None:
                return
            tmp_left = node.left
            tmp_right = node.right
            node.left, node.right = tmp_right, tmp_left
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)

        invert(root)

        return root
        
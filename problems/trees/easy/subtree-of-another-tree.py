# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Recursive(object):

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None: return True
        if root is None: return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            # Eligible to check left + right
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Neet(object):

    # 68% runtime, 63% memory
    # Damn the recursive solution here is so nice, got railroaded trying to implement this iteratively
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None: return True
        if root is None: return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left)) and (self.isSameTree(s.right, t.right))
        # Pass here if only 1 of s or t exists, or if s.val != t.val
        return False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # 5% runtime, 98% memory
    # Urgh the edge cases here - and not having the constraint of unique values in the tree mmmm
    # Lol brute force solution O(ST), S = # of nodes in root, T = # of nodes in subroot
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        # First look for subroot in root
        candidate_subroots = []
        stack = [root]

        def is_node_equal(node1, node2):
            if node1.val != node2.val:
                return False
            
            # Both exist
            if node1.left and node2.left:
                if node1.left.val != node2.left.val:
                    return False
            # Or either one exists
            elif node1.left or node2.left:
                return False

            # Both exist
            if node1.right and node2.right:
                if node1.right.val != node2.right.val:
                    return False
            # Or either one exists
            elif node1.right or node2.right:
                return False
            
            return True

        # Traverse through root and find all candidate subroots
        while stack:
            cur = stack.pop()
            if is_node_equal(cur, subRoot):
                candidate_subroots.append(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right) 

        if len(candidate_subroots) == 0:
            return False
        
        while candidate_subroots:
            stack, subroot_stack = [candidate_subroots.pop(0)], [subRoot]

            while stack and subroot_stack:
                cur1, cur2 = stack.pop(), subroot_stack.pop()
                if is_node_equal(cur1, cur2) == False:
                    # Proven false, skip to next iteration
                    stack.append(cur1)
                    subroot_stack.append(cur2)
                    break
                if cur1.left:
                    stack.append(cur1.left)
                if cur1.right:
                    stack.append(cur1.right)
                if cur2.left:
                    subroot_stack.append(cur2.left)
                if cur2.right:
                    subroot_stack.append(cur2.right)

            if len(stack) == 0 and len(subroot_stack) == 0:
                return True

        return False

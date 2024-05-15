# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# All Node.val are unique.
# p and q will exist in the BST.
# p != q

class Solution(object):

    # 92% runtime, 50% memory
    def lowestCommonAncestor_Recursive(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_Recursive(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_Recursive(root.left, p, q)
        else:
            return root

    # Damn, the code brevity here is gg
    # 76% runtime, 21% memory
    # No need for stack gg, because just update the pointer
    def lowestCommonAncestor_Neet(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
    

    # 51% memory, 21% runtime
    # Yea, this is a simpler implementation than the first recursive implementation I came up with, and less steps required
    # The idea is single walk - try to find path towards both. And if/when the path diverges, you have found the LCA.
    def lowestCommonAncestor_RecursiveV2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Let's make it recurse into itself, while doing a single walkdown
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        # Find next nodes towards p and q
        to_p, to_q = root, root
        if p.val < root.val:
            to_p = root.left
        else:
            to_p = root.right
        if q.val < root.val:
            to_q = root.left
        else:
            to_q = root.right
        
        if to_p.val != to_q.val:
            return root
        
        return self.lowestCommonAncestor_RecursiveV2(to_p, p, q)

    # 76.33 runtime, 78% memory
    def lowestCommonAncestor_Iterative(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Another way is to simultaneously walk towards each node
        path_p, path_q = [root], [root]
        
        while path_p[-1].val == path_q[-1].val:
            cur_p, cur_q = path_p[-1], path_q[-1]
            # Find next node for both
            if p.val < cur_p.val:
                path_p.append(cur_p.left)
            elif p.val > cur_p.val:
                path_p.append(cur_p.right)
            else:
                return p
            
            if q.val < cur_q.val:
                path_q.append(cur_q.left)
            elif q.val > cur_q.val:
                path_q.append(cur_q.right)
            else:
                return q
        
        # Diverged and equal length
        return path_p[-2]

    # Sighh........Had a correct idea within 5 minutes, but I got stuck on the implementation details for 30-40 minutes
    # 91% memory, 50% runtime
    # Issue 1 - [].append() 
        # Returns None, not the new list
        # In-place mutation of the list
        # Syntax is append(), not append[]
    # Issue 2 - p and q parameters are of TreeNode type, not number
    def lowestCommonAncestor_Recursive(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # According to constraints, target_val will always exist
        def find_path(node, target_val, path):
            path.append(node)
            # Add self to path
            if target_val == node.val:
                return path
            # Recurse into left if smaller
            if target_val < node.val:
                return find_path(node.left, target_val, path)  
            # Recurse into right if bigger
            elif node.right:
                return find_path(node.right, target_val, path)  
            # No == edge case to consider

        path_p = find_path(root, p.val, [])
        path_q = find_path(root, q.val, [])

        for i in range(min(len(path_p), len(path_q))):
            p_parent = path_p[i]
            q_parent = path_q[i]
            
            if p_parent.val == p.val:
                return p
            if q_parent.val == q.val:
                return q
            
            # Satisfy either of above, if reached end of path
            # So will have another node left in path
            if path_p[i + 1].val != path_q[i + 1].val:
                return p_parent
        
        return root
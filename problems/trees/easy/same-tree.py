# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # 61% runtime, 77% memory
    # OK - just don't use != or == operators with None type
    def isSameTree_IterativeDFSV2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        stack_p, stack_q = [p], [q]

        while stack_p and stack_q:
            node_p, node_q = stack_q.pop(), stack_q.pop()
            if not node_p and not node_q:
                pass
            elif not node_p or not node_q:
                return False
            elif node_p.val != node_q.val:
                return False

            if node_p:
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
            if node_q:
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)

        if stack_p or stack_q:
            return False
        
        return True

    # 56% runtime, 77% memory
    # Sigh recursive is so much easier, I see that instead of trying to use inequality operator for None, Neet just wrote out the explicit recursive base cases. Python was being really dodgy with != comparison for None objects. So let's just avoid it
    def isSameTree_Neet(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return (self.isSameTree_Neet(p.left, q.left) and 
                self.isSameTree_Neet(p.right, q.right))

    def isSameTree_BFS(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            vals_p, vals_q = [], []
            for _ in range(len(queue_p)):
                node = queue_p.popleft()
                vals_p.append(node)
                if node:
                    queue_p.append(node.left)
                    queue_p.append(node.right)
            for _ in range(len(queue_q)):
                node = queue_q.popleft()
                vals_q.append(node)
                if node:
                    queue_q.append(node.left)
                    queue_q.append(node.right)

            if len(vals_p) != len(vals_q):
                return False
            
            for i in range(len(vals_p)):
                val_p, val_q = vals_p[i], vals_q[i]
                if val_p and val_q:
                    if val_p.val != val_q.val:
                        return False
                elif val_p != val_q:
                    return False
                    
        if queue_p or queue_q:
            return False

        return True


    # Done in 14 minutes, 76% runtime, 100% memory
    # Meh, I don't feel too great about this implementation and time to do it. Got tripped up on some inconsistent behaviour for Python equality check
    def isSameTree_DFS(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            p_node = stack_p.pop()
            q_node = stack_q.pop()
            
            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
            elif p_node != q_node:
                return False

            if p_node:
                stack_p.append(p_node.left)
                stack_p.append(p_node.right)
            if q_node:
                stack_q.append(q_node.left)
                stack_q.append(q_node.right)

        if stack_p or stack_q:
            return False

        return True
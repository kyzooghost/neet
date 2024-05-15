# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # 912% memory, 77% memory - huh? deque is inherently more space and time efficient than list?
    def levelOrder_Neet(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque([root])
        resp = []

        while queue:
            queue_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                queue_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            resp.append(queue_values)
            
        return resp


    # 13% runtime, 77% memory
    # Just BFS traversal while tracking values of each height
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        resp = []

        while queue:
            queue_values = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                queue_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            resp.append(queue_values)
            
        return resp

        
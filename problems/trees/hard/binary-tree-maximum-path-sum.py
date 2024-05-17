# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.


class Solution_V2(object):
    # How can we do this in better than O(N^2) time
    # How can we achieve O(N) or O(N lg N) time?
    # Can we recursively reduce this to a subtree? What if we maintain the sum? Then know subtree contains the max path. Keep a pointer to the max subtree, and brute force within the max subtree 
    # mmm this solution didn't work because the max path is not constrained in a subtree - it can just be a node itself without considering any of its children.
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Add .parent to each TreeNode
        root.parent = None
        self.max_subtree_sum = float('-inf')
        self.max_subtree_ptr = None

        def add_sum_dfs(node):
            node.sum = node.val
            if node.left:
                node.left.parent = node
                node.sum += add_sum_dfs(node.left)
            if node.right:
                node.right.parent = node
                node.sum += add_sum_dfs(node.right)
            if node.sum > self.max_subtree_sum:
                self.max_subtree_sum = node.sum
                self.max_subtree_ptr = node
            return node.sum
        
        # Single walk through each node -> O(N) time
        # Add .sum and .parent properties
        add_sum_dfs(root)
        root.parent = None

        # Brute force through max_subtree_nodes

        # Global variables
        self.max_sum = float("-inf")
        subtree_node_list = []
        stack = [self.max_subtree_ptr]        
        while stack:
            cur = stack.pop()
            subtree_node_list.append(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        # DFS from each node
        def dfs(node, sum):
            new_sum = node.val + sum
            self.max_sum = max(new_sum, self.max_sum)
            self.visited[node] = True
            if node.left and node.left not in self.visited:
                dfs(node.left, new_sum)
            if node.right and node.right not in self.visited:
                dfs(node.right, new_sum)
            if node.parent and node.parent not in self.visited:
                dfs(node.parent, new_sum)      

        for node in subtree_node_list:
            self.visited = {}
            dfs(node, 0)

        return self.max_sum


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Oh man, this question is devious because you can't find the answer by traversing down the tree. Paths also include lateral movements.
    # I can think of a brute force O(N^2) solution - Add a link to each TreeNode to its parent, then DFS from every node and find the max sum
    # Ok got 92/96 test cases passing for Leetcode, but got Time Limited Exceeded error
    # So this solution works, but not time efficient enough
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Global variables
        self.max_sum = float("-inf")

        # Add .parent to each TreeNode
        root.parent = None

        # Maintain pointer to each node
        node_list = []
        
        # Preorder traversal
        stack = [root]        
        while stack:
            cur = stack.pop()
            node_list.append(cur)
            if cur.left:
                stack.append(cur.left)
                cur.left.parent = cur
            if cur.right:
                stack.append(cur.right)
                cur.right.parent = cur

        # DFS from each node
        def dfs(node, sum):
            new_sum = node.val + sum
            self.max_sum = max(new_sum, self.max_sum)
            self.visited[node] = True
            if node.left and node.left not in self.visited:
                dfs(node.left, new_sum)
            if node.right and node.right not in self.visited:
                dfs(node.right, new_sum)
            if node.parent and node.parent not in self.visited:
                dfs(node.parent, new_sum)      

        for node in node_list:
            self.visited = {}
            dfs(node, 0)

        return self.max_sum
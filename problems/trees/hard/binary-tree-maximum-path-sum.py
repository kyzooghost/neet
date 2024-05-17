# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class Solution_V5(object):
    # 60% memory, 20% runtime
    # Ok you can reduce it to subtrees, but finding the max path in each subtree - max subpath for L and R
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            l_max = max(dfs(node.left), 0)
            r_max = max(dfs(node.right), 0)

            self.res = max(self.res, node.val + l_max + r_max)
            return max(0, node.val + max(l_max, r_max))

        dfs(root)
        return self.res


class Solution_V4(object):
    # 60% memory, 73% runtime
    # Mmm yea ok so you can reduce it to finding l_max_path and r_max_path
    # 60% runtime, 50% memory
    def maxPathSum_Neet(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            l_max = dfs(node.left)
            r_max = dfs(node.right)
            l_max = max(l_max, 0)
            r_max = max(r_max, 0)
            self.res = max(self.res, node.val + l_max + r_max)
            return node.val + max(l_max, r_max)
        dfs(root)
        return self.res


class Solution_V3(object):
    # 60% memory, 73% runtime
    # Mmm yea ok so you can reduce it to finding l_max_path and r_max_path
    def maxPathSum_AfterVideo(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("-inf")

        def dfs(node):
            l_max_path, r_max_path = 0, 0

            # Go into left
            if node.left:
                l_max_path = dfs(node.left)
            if node.right:
                r_max_path = dfs(node.right)

            # Possibilities - node.val, node.val + L, node.val + R, node.val + L + R
            self.res = max(node.val, node.val + l_max_path, node.val + r_max_path, node.val + l_max_path + r_max_path)

            # Return max subpath contribution - node itself, nothing, node.val + L, node.val + R
            return max(node.val, node.val + l_max_path, node.val + r_max_path, 0)

        dfs(root)

        return self.res


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
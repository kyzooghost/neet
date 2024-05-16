# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heappop

class Solution_Neet(object):
    # Lol styled with this code brevity
    # 55% runtime, 51% memory
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Deal with it recursively
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        inorder_index = inorder.index(preorder[0])
        # L partition of preorder
        root.left = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])
        return root

class Solution_V2(object):
    # Watched Neet video, ok the key insight is that we don't actually have to look for the min preorder indexes - the partition size of inorder == partition size of preorder - L + R + M = M + L + R
    # 88% runtime, 86% memory - O(N) time and O(N) space
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Deal with it recursively
        if len(preorder) == 0:
            return None
        
        self.inorder_dict, self.preorder_dict = {}, {}
        # num => index
        self.inorder_global = inorder
        self.preorder_global = preorder
        
        for i in range(len(inorder)):
            self.inorder_dict[inorder[i]] = i
            self.preorder_dict[preorder[i]] = i

        root = TreeNode(preorder[0])
        return self.dfs(root, 0, len(preorder) - 1)

    # l = min inorder_index, r = max inorder_index
    def dfs(self, node, l, r):
        if l >= r:
            return node

        # Get inorder index
        inorder_index = self.inorder_dict[node.val]
        preorder_index = self.preorder_dict[node.val]

        l_partition_size = 0
        if inorder_index > l:
            l_partition_size = inorder_index - l
            l_min_preorder_index = preorder_index + 1
            num = self.preorder_global[l_min_preorder_index]
            node.left = self.dfs(TreeNode(num), l, inorder_index - 1)

        if inorder_index < r:
            r_min_preorder_index = preorder_index + l_partition_size + 1
            num = self.preorder_global[r_min_preorder_index]
            node.right = self.dfs(TreeNode(num), inorder_index + 1, r)

        return node

class Solution_V1(object):
    # 5% runtime, 5% memory, lolz same as below
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Deal with it recursively
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        # O(N) populating dict
        # num => inorder_index, num => preorder_index
        self.inorder_dict, self.preorder_dict = {}, {}
        self.inorder_global = inorder
        
        for i in range(len(preorder)):
            self.preorder_dict[preorder[i]] = i
            self.inorder_dict[inorder[i]] = i

        return self.dfs(root, 0, len(preorder) - 1)


    # l = min inorder_index, r = max inorder_index, m = current node inorder_index
    def dfs(self, node, l, r):
        if l >= r:
            return node

        inorder_index = self.inorder_dict[node.val]

        # For L and R, find node (lowest preorder index) and recurse
        if inorder_index > l:
            pq = []
            for i in range(l, inorder_index):
                num = self.inorder_global[i]
                heappush(pq,(self.preorder_dict[num], num))
            
            node.left = self.dfs(TreeNode(heappop(pq)[1]), l, inorder_index - 1)

        if inorder_index < r:
            pq = []
            for i in range(inorder_index + 1, r + 1):
                num = self.inorder_global[i]
                heappush(pq,(self.preorder_dict[num], num))
            
            node.right = self.dfs(TreeNode(heappop(pq)[1]), inorder_index + 1, r)

        return node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # Yep, stumped by this for more than 2hrs
    # And then even when I was trying recursive approach, prob took 2 hrs to come up with the solution
    # 5% runtime, 88% memory
    # Kept trying to solve this by iterating through preorder list, but couldn't solve whether to determine the next node would be on the immediate right, or a parent's right
    # This is an O(N lg N) time efficiency, O(N) space efficiency approach
    # This recursive implementation is so much code already zzz
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Deal with it recursively
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])

        # O(N) populating dict
        # num => inorder_index, num => preorder_index
        self.inorder_dict, self.preorder_dict = {}, {}
        self.inorder_global = inorder
        
        for i in range(len(preorder)):
            self.preorder_dict[preorder[i]] = i
            self.inorder_dict[inorder[i]] = i

        return self.dfs(root, 0, len(preorder) - 1)


    # l = min inorder_index, r = max inorder_index, m = current node inorder_index
    def dfs(self, node, l, r):
        if l >= r:
            return node

        inorder_index = self.inorder_dict[node.val]

        # For L and R, find node (lowest preorder index) and recurse
        if inorder_index > l:
            # Find lowest preorder index
            min_preorder_index = 3001
            min_preorder_num = None
            # Iterate through [l, inorder_index - 1]
            for i in range(l, inorder_index):
                # Index => num
                num = self.inorder_global[i]
                # num => preorder index
                if self.preorder_dict[num] < min_preorder_index:
                    min_preorder_index = self.preorder_dict[num]
                    min_preorder_num = num
            node.left = self.dfs(TreeNode(min_preorder_num), l, inorder_index - 1)
        
        if inorder_index < r:
            # Find lowest preorder index
            min_preorder_index = 3001
            min_preorder_num = None
            # Iterate through [l, inorder_index - 1]
            for i in range(inorder_index + 1, r + 1):
                # Index => num
                num = self.inorder_global[i]
                # num => preorder index
                if self.preorder_dict[num] < min_preorder_index:
                    min_preorder_index = self.preorder_dict[num]
                    min_preorder_num = num
            node.right = self.dfs(TreeNode(min_preorder_num), inorder_index + 1, r)
            
        return node
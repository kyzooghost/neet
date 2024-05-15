# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isValidBST_IterativeV3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Lol inorder iterative requires a pointer
        # Preorder you can initialize root in the stack, because root is first to visit
        # You cannot initialize root to stack for inorder or postorder
        ptr, stack, last_val = root, [], None

        while stack:
            stack.append(ptr)
            while ptr.left:
                ptr = ptr.left
                stack.append(ptr)
            
            

                stack.append(ptr)

        # while ptr or stack:
        #     if ptr:
        #         stack.append(ptr)
        #         ptr = ptr.left
        #     else:
        #         ptr = stack.pop()
        #         if last_val is not None:
        #             if ptr.val <= last_val:
        #                 return False
        #         last_val = ptr.val
        #         ptr = ptr.right


        return True



    # 62% runtime, 43% memory
    # Wow, inorder iterative is so different from preorder, need a ptr and I have to let it go to null?
    def isValidBST_IterativeV2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ptr, stack, last_val = root, [], None
        while ptr or stack:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack.pop()
                if last_val is not None:
                    if ptr.val <= last_val:
                        return False
                last_val = ptr.val
                ptr = ptr.right
        return True


    # 85% runtime, 43% memory
    def isValidBST_Iterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Lol preorder iterative requires a pointer
        ptr, stack, vals = root, [], []
        while ptr or stack:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack.pop()
                if len(vals) > 0 and ptr.val <= vals[-1]:
                    return False
                vals.append(ptr.val)
                ptr = ptr.right
        return True
    
    # Improvement over V1, in that we can check the existing vals_list as we go
    # Still O(N) extra space
    # 61% runtime, 14% memory
    def isValidBST_RecursiveV2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        # Ok we can use in-order traversal and O(N) space to do this
        def dfs(node, vals_list):
            l, r = True, True
            if node.left:
                l = dfs(node.left, vals_list)
            if len(vals_list) > 0 and node.val <= vals_list[-1]:
                return False
            vals_list.append(node.val)
            if node.right:
                r = dfs(node.right, vals_list)
            return l and r

        vals = []
        return dfs(root, vals)

    # 28% runtime, 7% memory and 1 hour to come up with a working solution :(
    # Urgh first two approaches I had failed, and I was struggling with implementing inorder traversal
    def isValidBST_Recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        # Ok we can use in-order traversal and O(N) space to do this
        def dfs(node, vals_list):
            if node.left:
                dfs(node.left, vals_list)
            vals_list.append(node.val)
            if node.right:
                dfs(node.right, vals_list)

        vals = []
        dfs(root, vals)
        
        if len(vals) == 1:
            return True
        
        for i in range(1, len(vals)):
            if vals[i] <= vals[i - 1]:
                return False

        return True

    # Only works if invalid nodes are only one level apart
    # Need to track min and max for L + R subtrees as well
    def isValidBST_SingleLevel(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left:
            if root.left.val >= root.val:
                return False
        if root.right:
            if root.right.val <= root.val:
                return False
        
        l, r = True, True
        if root.left:
            l = self.isValidBST_SingleLevel(root.left)
        if root.right:
            r = self.isValidBST_SingleLevel(root.right)
        return l and r
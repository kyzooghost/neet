# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def isValidBST_RecursiveV4(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        # Ok we can use in-order traversal and O(N) space to do this
        last_val = None

        def dfs(node):
            l, r = True, True
            if node.left:
                l = dfs(node.left)
            if last_val is not None and node.val <= last_val:
                return False
            last_val = node.val
            if node.right:
                r = dfs(node.right)
            return l and r

        return dfs(root)


    # Where did I get stuck?
        # 1. Not good enough to just compare node.val to node.left & node.right, violating node may be more than 1 level away
        # 2. Wrong rabbit hole to obtain min and max of each subtree
        # 3. float("inf") for infinity, float("-inf") for negative infinity
        # 4. Haven't seen iterative implementation for inorder traversal before
        # 5. Haven't used inorder traversal - either recursive or iterative - to collect numbers from a BST
        # 6. Need to be more comfortable with letting the node pointer go to None. You just have to do null check at the start of each loop.
        # 7. Even if you use inorder traversal, no need to keep entire val list, just the last val visited

    # 89% runtime, 63% memory
    # Damn...didn't even need to worry about inorder traversal
    # Pass valid L + R boundary with each recursive call, and check against these in each call
    def isValidBST_Neet(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, left, right):
            if not node:
                return True
            if node.val >= right:
                return False
            if node.val <= left:
                return False
            
            return (valid(node.left, left, node.val) and
                valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))


    def isValidBST_RecursiveV3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 48% runtime, 7% memory - Ok does work but is pretty bad lol
        # Just do in-order traversal and compare to last value traversed
        # This is too complicated trying this 'compare min/max of entire subtree to current node or other subtree' approach. Wrong rabbit hole.
        def dfs(node):
            l_min, r_min = float("inf"), float("inf")
            l_max, r_max = float("-inf"), float("-inf")
            l_check, r_check = True, True

            if node.left:
                l_check, l_min, l_max = dfs(node.left)
            if node.right:
                r_check, r_min, r_max = dfs(node.right)
            
            if l_max >= node.val or l_max >= r_min:
                l_check = False
            if r_min <= node.val or r_min <= l_max:
                r_check = False

            return (
                l_check and r_check,
                min(node.val, l_min, r_min),
                max(node.val, l_max, r_max),
            )
                
        check, _, _  = dfs(root)
        return check        

    # 62% runtime, 43% memory
    # Wow, inorder iterative is so different from preorder, need a ptr and I have to let it go to null?
    # Sigh alright, accept that inorder iterative will not be as neat as preorder iterative - need to track a ptr variable and let it be null
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
                if last_val is not None and ptr.val <= last_val:
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
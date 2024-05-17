# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CodecV2:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(",")

        self.i = 0
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            else:
                node = TreeNode(int(vals[self.i]))
                self.i += 1
                node.left = dfs()
                node.right = dfs()
                return node

        return dfs()

class Codec_Neet:
    # 74% runtime, 80% memory
    # Again...recursive to save the day
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        

class Codec_NeetWatched:

    # Ahh I see, keeping track of None in traversals is key here
    # 20% runtime, 15% runtime - Don't feel like I dealt with deserialization neatly
    # Implementation is tricky here, took ms 29 mins even with the main idea
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ""
        
        preorder, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                preorder.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                preorder.append('N')
        return ','.join(str(x) for x in preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == "":
            return None
        preorder = data.split(',')
        ptr = root = TreeNode(preorder[0])
        stack = []
        print(preorder, len(preorder))
        
        for i in range(1, len(preorder) - 2):
            print(i)
            # Reached leaf node - N->N
            if preorder[i] == 'N' and preorder[i - 1] == 'N':
                ptr = stack.pop()
            # If number preceding - Num -> Num
            elif preorder[i] != 'N' and preorder[i - 1] != 'N':
                ptr.left = TreeNode(preorder[i])
                stack.append(ptr)
                ptr = ptr.left
            # Is a right node - N -> Num
            elif preorder[i] != 'N' and preorder[i - 1] == 'N':
                ptr.right = TreeNode(preorder[i])
                ptr = ptr.right
            # Num -> N
            else:
                pass

        return root
        

class CodecV1:

    # Damnnnnn I did it. Implemented this in 33 mins with help of print statements
    # 34% runtime, 58% memory
    # Not a clean solution though, especially deserializing the BFS string
    # Problem with inorder + preorder construction is that this question doesn't respect the constraint of unique node values
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        queue = [root]
        bfs = []
        while queue:
            bfs_level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    bfs_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    bfs_level.append('null')
            bfs_level_serialized = ','.join(str(x) for x in bfs_level)
            bfs.append(bfs_level_serialized)
        
        return '+'.join(str(x) for x in bfs)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        bfs = data.split('+')
        root = TreeNode(bfs[0])
        nodes_bfs = [[root]]

        for i in range(0, len(bfs) - 1):
            # Initialize child nodes
            child_nodes = []
            child_vals = bfs[i+1].split(',')

            for val in child_vals:
                if val == 'null':
                    child_nodes.append(None)
                else:
                    child_nodes.append(TreeNode(val))

            # Iterate through current level nodes
            counter = 0
            for node in nodes_bfs[i]:
                if node:
                    l_index = counter * 2
                    node.left = child_nodes[l_index]
                    r_index = 1 + counter * 2
                    node.right = child_nodes[r_index]
                    counter += 1
            nodes_bfs.append(child_nodes)
            
        return root


# Ok I learned that I was doing preorder traversal all wrong
# Got a solution that passed for 11/53 cases in 40 minutes, with a lot of silly syntax errors on the way
# Mmm thing with preorder + inorder traversal was that they had no duplicate values there hmmmm.
# Ok what if we do BFS, but track the null nodes mmm
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # Well we can just serialize the inorder + preorder traversal results, deserialize that and do the 'construct-binary-tree-from-preorder-and-inorder' problem
        # O(N) to populate both
        if root is None:
            return '+'
        preorder = []
        inorder = []

        # Populate preorder
        stack = [root]
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        # Populate inorder
        ptr, stack = root, []
        while ptr or stack:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                node = stack.pop()
                inorder.append(node.val)
                ptr = node.right

        # Serialize preorder + inorder
        preorder_serialized = ','.join(str(x) for x in preorder)
        inorder_serialized = ','.join(str(x) for x in inorder)
        return preorder_serialized + '+' + inorder_serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Edge case of no nodes
        
        if data == '+':
            return None
        split_data = data.split('+')
        self.preorder = split_data[0].split(',')
        self.inorder = split_data[1].split(',')
        print(self.preorder)
        print(self.inorder)


        self.inorder_dict, self.preorder_dict = {}, {}
        for i in range(len(self.inorder)):
            # Can have duplicate nums...
            self.inorder_dict[self.inorder[i]] = i
            self.preorder_dict[self.preorder[i]] = i

        def dfs(node, inorder_l, inorder_r):
            if inorder_l >= inorder_r:
                return node
            inorder_index = self.inorder_dict[node.val]
            preorder_index = self.preorder_dict[node.val]

            l_partition_size = 0
            if inorder_index > inorder_l:
                l_partition_size = inorder_index - inorder_l
                l_min_preorder_index = preorder_index + 1
                num = self.preorder[l_min_preorder_index]
                node.left = dfs(TreeNode(num), inorder_l, inorder_index - 1)

            if inorder_index < inorder_r:
                r_min_preorder_index = preorder_index + l_partition_size + 1
                num = self.preorder[r_min_preorder_index]
                node.right = dfs(TreeNode(num), inorder_index + 1, inorder_r)

            return node
        
        root = TreeNode(self.preorder[0])
        return dfs(root, 0, len(self.preorder) - 1)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

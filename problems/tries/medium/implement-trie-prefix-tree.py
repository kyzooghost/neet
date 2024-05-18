class Node(object):
    def __init__(self):
        self.root = None
        self.children = [None] * 26
        self.isWord = False

# 28% runtime, 64% memory, done in 11 minutes :))
# But I have memories of grasping the verkle trie in Ethereum so this is something I've delved into deeply before
class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self.root
        for char in word:
            index = ord(char) - ord("a")
            # Child exists, update pointer
            if ptr.children[index]:
                pass
            # Else must create child
            else:
                ptr.children[index] = Node()
            ptr = ptr.children[index]
        ptr.isWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ptr = self.root
        for char in word:
            index = ord(char) - ord("a")
            # Child exists, update pointer
            if ptr.children[index]:
                ptr = ptr.children[index]
            # Else does not exist
            else:
                return False
        return ptr.isWord
        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        ptr = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            # Child exists, update pointer
            if ptr.children[index]:
                ptr = ptr.children[index]
            # Else must create child
            else:
                return False
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

print(ord("z") - ord("a"))
print([None] * 26)
# Sighhhhhh mad, had the idea coded within 12 minutes, but got flustered by off-by-one error for the next 20 minutes and only got a running solution at 32 minutes zzzz
# 16% runtime, 58% memory
class Node(object):
    def __init__(self):
        self.root = None
        self.children = [None] * 26
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
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
        def dfs_search(node, word_index):
            if node is None:
                return False
            if word_index == len(word):
                return node.isWord
            char = word[word_index]
            if char == ".":
                resp = False
                for child in node.children:
                    resp = resp or dfs_search(child, word_index + 1)
                return resp
            else:
                index = ord(char) - ord("a")
                return dfs_search(node.children[index], word_index + 1)

        return dfs_search(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
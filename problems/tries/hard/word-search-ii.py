class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self
        for char in word:
            index = ord(char) - ord("a")
            if not ptr.children[index]:
                ptr.children[index] = TrieNode()
            ptr = ptr.children[index]
        ptr.isWord = True

# Hmm, are the hints saying to make a trie of all words?
# Then check the current prefix as you go along? Stop backtracking not in trie? Hmm
# Lol got test passes cased, but time limit exceeded. And I'm already passing the raw trie pointer in the dfs
# Wow had to submit and make small optimizations maybe 5 times to get this solution in
class Solution_V2(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        x_length, y_length = len(board[0]), len(board)
        # (tuple) => True
        self.visited = {}
        self.found = set()

        def dfs(i, j, cur_word, trie_ptr):
            # Out of board
            if i < 0 or i >= x_length:
                return
            if j < 0 or j >= y_length:
                return
            # Previsited
            if (i, j) in self.visited:
                return
            
            board_letter = board[j][i]
            letter_index = ord(board_letter) - ord("a")
            new_ptr = trie_ptr.children[letter_index]
            if new_ptr is None:
                return
            
            new_word = cur_word + board_letter
            if new_ptr.isWord is True:
                self.found.add(new_word)

            self.visited[(i,j)] = True
            # Walk into all 4 directions - O(4^(len(word)))
            dfs(i - 1, j, new_word, new_ptr)
            dfs(i + 1, j, new_word, new_ptr)
            dfs(i, j - 1, new_word, new_ptr)
            dfs(i, j + 1, new_word, new_ptr)
            del self.visited[(i,j)]

        for y in range(y_length):
            for x in range(x_length):
                dfs(x, y, "", trie)

        return list(self.found)
        

sln = Solution_V2()
board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]

print(sln.findWords(board, words))

# How could we use a trie? If we use the backtracking approach to instead create a trie, and then search for words in the trie - would be O(M^2 N^2) time complexity, rather than O(M^2 N^2 len(words))
# Well this approach is still TLE lol
class Solution_V1(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        resp = []
        self.dict = {}
        x_length = len(board[0])
        y_length = len(board)
        self.visited = {}

        def dfs(i, j, cur_word):
            # Out of board
            if i < 0 or i >= x_length:
                return
            if j < 0 or j >= y_length:
                return
            # Already visited on this walk
            if (i, j) in self.visited:
                return
            
            board_letter = board[j][i]
            new_word = cur_word + board_letter
            self.dict[new_word] = True

            self.visited[(i,j)] = True
            # Walk into all 4 directions - O(4^(len(word)))
            dfs(i - 1, j, new_word)
            dfs(i + 1, j, new_word)
            dfs(i, j - 1, new_word)
            dfs(i, j + 1, new_word)
            del self.visited[(i,j)]

        for y in range(y_length):
            for x in range(x_length):
                dfs(x, y, "")

        for word in words:
            if word in self.dict:
                resp.append(word)

        return resp

# Well brute force with word-search solution gets TLE as expected - 42/65 test cases passing
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Umm, can I not just brute force this with a word-search solution adjusted for a list of words?
        # How would I use a trie here?
        # Let's just implement the brute force

        self.resp = []

        x_length = len(board[0])
        y_length = len(board)
        # (tuple) => True
        self.visited = {}
        self.found = {}

        def dfs(i, j, word_index, word):
            # Found a match
            if word in self.found:
                return
            # Out of board
            if i < 0 or i >= x_length:
                return
            if j < 0 or j >= y_length:
                return
            
            board_letter = board[j][i]
            word_char = word[word_index]

            # Did not walk onto the right letter
            if board_letter != word_char:
                return

            if (i, j) in self.visited:
                return
            
            # Found last letter
            if word_index == len(word) - 1:
                self.found[word] = True
                self.resp.append(word)
                return

            self.visited[(i,j)] = True
            # Walk into all 4 directions - O(4^(len(word)))
            dfs(i - 1, j, word_index + 1, word)
            dfs(i + 1, j, word_index + 1, word)
            dfs(i, j - 1, word_index + 1, word)
            dfs(i, j + 1, word_index + 1, word)
            del self.visited[(i,j)]

        for word in words:
            for y in range(y_length):
                for x in range(x_length):
                    dfs(x, y, 0, word)

        return self.resp
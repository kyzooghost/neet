
class Solution_Neet(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        

# 18% runtime, 81% memory, done in 23 minutes :)
# Easier to break down into recursive case - walk onto each node
# And easier to deal with null cases on base case checks, rather than avoiding walk into null
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.resp = False

        x_length = len(board[0])
        y_length = len(board)
        # (tuple) => True
        self.visited = {}

        def dfs(i, j, word_index):
            # Found a match
            if self.resp == True:
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

            # How to check if previsited?
            if (i, j) in self.visited:
                return
            
            # Found last letter
            if word_index == len(word) - 1:
                self.resp = True
                return

            self.visited[(i,j)] = True
            # Walk into all 4 directions - O(4^(len(word)))
            dfs(i - 1, j, word_index + 1)
            dfs(i + 1, j, word_index + 1)
            dfs(i, j - 1, word_index + 1)
            dfs(i, j + 1, word_index + 1)
            del self.visited[(i,j)]

        for y in range(y_length):
            for x in range(x_length):
                dfs(x, y, 0)

        return self.resp

        
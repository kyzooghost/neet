from collections import defaultdict

# Well, much cleaner code at the expense of space complexity
# O(N^2) space, O(N^2) time
class Solution_Neet(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        rows_set, cols_set, square_set = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in rows_set[r] or board[r][c] in cols_set[c] or board[r][c] in square_set[(r // 3, c // 3)]:
                    return False
                else:
                    rows_set[r].add(board[r][c])
                    cols_set[c].add(board[r][c])
                    square_set[(r // 3, c // 3)].add(board[r][c])
        
        return True

# Hmm check each row, column and square
# You can use a set for each row, column and square

# If you check each row, then column, then square.
# That is O(N) space - O(N^2) time
# Alright 65% runtime, 93% memory so decent solution on first attempt
# Can probably be a lot cleaner with the code hmm, so let's watch Neet for that

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        num_set = set()

        # Iterate across rows
        for r in range(rows):
            num_set.clear()
            for c in range(cols):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in num_set:
                    return False
                else:
                    num_set.add(board[r][c])

        # Iterate across cols
        for c in range(cols):
            num_set.clear()
            for r in range(rows):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in num_set:
                    return False
                else:
                    num_set.add(board[r][c])
        
        # Iterate across squares
        for i in range(3):
            for j in range(3):
                num_set.clear()
                starting_i, starting_j = 3*i, 3*j
                for x in range(starting_i, starting_i + 3):
                    for y in range(starting_j, starting_j + 3):
                        if board[x][y] == '.':
                            continue
                        elif board[x][y] in num_set:
                            return False
                        else:
                            num_set.add(board[x][y])
                    
        return True

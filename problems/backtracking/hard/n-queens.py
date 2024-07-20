
# Fair assumption that there must be 1 queen in the first row
# So that limits your trials to each square in the first row
# Then you need a subfunction to fill in the the board for that trial
# How to represent diagonal moves?

# Each trial
# Keep track of how many Queens
# Place Queen -> Place X
# Iterate until get . -> Place Queen again

# Place Queen -> 
# Time complexity - Iterate through whole board 2N times -> O(N^3) time complexity, O(N^2) space complexity
# Ah hmm...this works to find one solution, but what if there are multiple solutions for each 'starting' spot, then I need to backtrack

# Fill one row -> recurse into next row with backtracking, so need to be able to undo mmm
# O(1) diagonal check?
# (r-c) is constant for one diagonal, (r+c) is constant for another diagonal

# Dang - ~69 minutes to get first successful submission with 50% runtime and 12.5% memory
# Well glad that I got it without looking at solutions or discussion
# The thing that was eluding me was the O(1) diagonal check, if I had just known that 'r-c' is constant for one diagonal and 'r+c' is constant for the other diagonal
# And I coded up a whole other solution without backtracking that works to find one solution lmao
# With minor optimizations - remove row_set data structure, remove num_queens recursive function param -> get 80% runtime, 41% memory
class Solution_V2(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        resp = []

        # Don't need row_set, because iterating r+1 each time anyway
        col_set = set()
        diag_1_set = set() # r - c
        diag_2_set = set() # r + c
        
        def serialize_board(board):
            serialized_board = []
            for row in range(n):
                serialized_board.append("".join(board[row])) 
            return serialized_board

        # Place queen
        def recurse(board, r, c):
            # Don't need out of bounds check
            # Cannot place queen
            if c in col_set or r - c in diag_1_set or r + c in diag_2_set: return
            
            # Place queen
            board[r][c] = "Q"
            col_set.add(c)
            diag_1_set.add(r-c)
            diag_2_set.add(r+c)

            # Reached final row
            if n == r + 1:
                resp.append(serialize_board(board))
            else:
                # Recurse into next row
                for i in range(n):
                    recurse(board, r+1, i)

            # Backtrack
            board[r][c] = "."
            col_set.discard(c)
            diag_1_set.discard(r-c)
            diag_2_set.discard(r+c)
        
        # Try each starting position
        board = [["." for _ in range(n)] for _ in range(n)]
        for i in range(n):
            recurse(board, 0, i)

        return resp

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def placeX(board, r, c):
            if r < 0 or c < 0 or r >= n or c >= n: return
            if board[r][c] == ".": board[r][c] = "X"

        def placeQueen(board, r, c):
            board[r][c] = "Q"

            for i in range(n):
                placeX(board, r, i)
                placeX(board, i, c)
                placeX(board, r+1, c+1)
                placeX(board, r+1, c-1)
                placeX(board, r-1, c+1)
                placeX(board, r-1, c-1)

        def reprocessBoard(board_to_parse):
            for row in range(n):
                for col in range(n):
                    if board_to_parse[row][col] == "X": board_to_parse[row][col] = "."
            
            tmp = []
            for row in range(n):
                tmp.append("".join(board_to_parse[row])) 
            board_to_parse = tmp
            return tmp

        def trial(c):
            # Create board
            new_board = [["." for _ in range(n)] for _ in range(n)]
            # Place first queen
            placed_queen_count = 1
            placeQueen(new_board, 0, c)

            # Iterate through rows, starting from 2nd
            for row in range(1, n):
                for col in range(n):
                    if new_board[row][col] == ".":
                        placed_queen_count += 1
                        placeQueen(new_board, row, col)

            # Reprocess board
            if placed_queen_count == n: new_board = reprocessBoard(new_board)

            # Return
            return (placed_queen_count, new_board)
        
        resp = []
        # Trial for each position in first row
        for i in range(n):
            queen_count, trial_board = trial(i)
            if queen_count == n: resp.append(trial_board)
        return resp
        
sln = Solution_V2()
print(sln.solveNQueens(1))
print(sln.solveNQueens(4))

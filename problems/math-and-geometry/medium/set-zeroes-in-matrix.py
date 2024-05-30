# Same concept as what I was implementing, but a little cleaner
# Only need single extra variable, and can use 0 as the marker
class Solution_Neet(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0: row_zero = True
                    else: matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(0, rows):
                matrix[r][0] = 0

        if row_zero: matrix[0] = [0 for _ in range(cols)]

# 70% runtime, 71% memory - Ran into snags with 1 == True in Python gg
# Should not use True or False as delete marker in Python, because 1 == True
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_one, col_one = False, False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0: row_one = True
                    if c == 0: col_one = True
                    matrix[r][0] = "x"
                    matrix[0][c] = "x"
        for r in range(1, rows, 1):
            if matrix[r][0] == "x":
                matrix[r] = [0 for _ in range(cols)]

        for c in range(1, cols, 1):
            if matrix[0][c] == "x":
                for r in range(rows): matrix[r][c] = 0
        
        if row_one: matrix[0] = [0 for _ in range(cols)]
        if col_one: 
            for r in range(rows): matrix[r][0] = 0
a = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
b = [
  [0,1],
  [1,1]
]
c = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

sln = Solution()
print(sln.setZeroes(c))
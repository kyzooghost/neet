# Hmm, slightly easier implementation using squares
class Solution_Neet(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, cols - 1
        while l < r:
            # Solve square subproblem
            for i in range(r - l):
                top, bottom = l, r

                top_left = matrix[top][l+i]
                # Bottom left -> top left
                matrix[top][l+i] = matrix[bottom-i][l]
                # bottom right -> bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # top right -> bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                # top left -> top right =
                matrix[top+i][r] = top_left
            l += 1
            r -= 1

# 99% runtime, 47% memory
class Solution_V3(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose is just flip the matrix across a diagonal line...
        rows, cols = len(matrix), len(matrix[0])
        l, cur_row = 1, 0
        
        # Transpose
        while l < cols:
            for i in range(l, cols):
                tmp = matrix[cur_row][i]
                matrix[cur_row][i] = matrix[i][cur_row]
                matrix[i][cur_row] = tmp
            cur_row += 1
            l += 1

        # Reverse
        for r in range(rows):
            c = 0
            while c < cols - c - 1:
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][cols - c - 1]
                matrix[r][cols - c - 1] = tmp
                c += 1
        
# Transpose and reverse matrix rows
class Solution_V2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # * is the unpacking operator - [[1,2], [3,4]] becomes [1,2], [3,4]
        # zip -> returns iterator of tuples, so [1,2], [3,4] -> [(1, 3), (2, 4)]
        # map(list, zip(*matrix)) -> map each tuple to a list, so [(1, 3), (2, 4)] -> [[1,3], [2,4]]
        # Doesn't work for Leetcode - print(matrix) returns the rotated matrix but I think because the original memory pointer has not been altered
        matrix = list(map(list, zip(*matrix)))
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            c = 0
            while c < cols - c - 1:
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][cols - c - 1]
                matrix[r][cols - c - 1] = tmp
                c += 1

# (x, y) -> (y, -x)
# matrix[r][c] -> matrix[c][rows - r - 1]
# In-place rotation hmm
# Square matrix hmm
# Ok I worked out the formula for 90 degree rotation, but how to do this in O(1) space?
# Rotation loops?
# Holy shit, the first test and submission worked. Probably spent 40-50 mins wrapping my head around this and working through the various subproblems
    # 88% runtime, 47% memory
    # 1.) How to do a 90 degree rotation for any matrix element -> matrix[r][c] becomes matrix[c][rows-r-1]
    # 2.) How to rotate the matrix in-place with O(1) space
# But probably an easier way to do this - my first solution is way too hard to come up with in 30-minutes

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        # Rotate all 4 connected squares in the matrix
        def rotatePartial(r, c):
            cur_r, cur_c = r, c
            # Save next
            next = matrix[cur_r][cur_c]
            for _ in range(4):
                # Save next
                tmp = matrix[cur_c][rows - cur_r - 1]
                # Overwrite next
                matrix[cur_c][rows - cur_r - 1] = next
                # Update pointers
                tmp_cur_r = cur_r
                cur_r = cur_c
                cur_c = rows - tmp_cur_r - 1
                next = tmp

        l, r = 0, cols - 1
        cur_row = 0
        while l < r:
            for i in range(l, r):
                rotatePartial(cur_row, i)
            l += 1
            r -= 1
            cur_row += 1
        return matrix

sln = Solution_Neet()
print(sln.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(sln.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

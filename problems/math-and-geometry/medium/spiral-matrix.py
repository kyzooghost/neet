# 96% runtime, 41% memory
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        resp = []

        turn = 0
        while top <= bottom and left <= right:
            # Top (right sweep)
            if turn % 4 == 0:
                for i in range(left, right + 1):
                    resp.append(matrix[top][i])
                top += 1
            # Right (down sweep)
            elif turn % 4 == 1:
                for i in range(top, bottom + 1):
                    resp.append(matrix[i][right])
                right -= 1
            # Bottom (left sweep)
            elif turn % 4 == 2:
                for i in range(right, left - 1, -1):
                    resp.append(matrix[bottom][i])
                bottom -= 1
            # Left (up sweep)
            else:
                for i in range(bottom, top - 1, -1):
                    resp.append(matrix[i][left])
                left += 1
            turn += 1

        return resp

sln = Solution()
print(sln.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
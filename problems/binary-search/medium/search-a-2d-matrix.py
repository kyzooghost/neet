# Well you're just binary searching in 2-dimensions
# But the twist is searching for the row - it is a range rather than a single number
# Failed first submission because didn't consider the twist :(
# 81% runtime, 99.8% memory in <15 minutes
# Improved after watching Neet - 94% runtime, 96% memory
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])
        t, l = 0, 0
        b, r = rows - 1, cols - 1

        # First binary search for correct row
        mid_row = None
        while t <= b:
            mid_row = (t + b) // 2
            if target == matrix[mid_row][0]:
                return True
            elif target < matrix[mid_row][0]:
                b = mid_row - 1
            elif target > matrix[mid_row][-1]:
                t = mid_row + 1
            # Else in this row
            else:
                break
        if t > b: return False

        # Then binary search within row
        while l <= r:
            mid_col = (l + r) // 2
            if target == matrix[mid_row][mid_col]:
                return True
            elif target < matrix[mid_row][mid_col]:
                r = mid_col - 1
            else:
                l = mid_col + 1

        return False
    
sln = Solution()
print(sln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(sln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))


# print(sln.searchMatrix())
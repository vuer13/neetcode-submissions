class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1
        middle = (bottom - top) // 2
        while top <= bottom:
            middle = top + (bottom - top) // 2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][n - 1]:
                top = middle + 1
            else:
                break
        
        rowToLookAt = matrix[middle]
        left, right = 0, n - 1
        m = (right - left) // 2
        while left <= right:
            m = left + (right - left) // 2
            if target == rowToLookAt[m]:
                return True
            elif target > rowToLookAt[m]:
                left = m + 1
            else:
                right = m - 1

        return False

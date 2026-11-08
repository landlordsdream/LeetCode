class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n -1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            val =  matrix[row][col]
            if val == target:
                return True
            if val > target:
                right -= 1
            if val < target:
                left += 1
        return False

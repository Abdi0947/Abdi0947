# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=set()
        col=set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        for nr in row:
            for nc in range(len(matrix[0])):
                matrix[nr][nc]=0
        for nc in col:
            for nr in range(len(matrix)):
                matrix[nr][nc]=0
                   
        return matrix
sol=Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(sol.setZeroes(matrix))
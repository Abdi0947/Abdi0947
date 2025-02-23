# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        matrix.reverse()

        for i in range(row):
            for j in range(i+1,col):
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
        return matrix
sol=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.rotate(matrix))
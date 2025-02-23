# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        col = len(matrix[0])
        row = len(matrix)
        answer = [[0] * row for _ in range(col)] 
        
        for i in range(row): 
            for j in range(col): 
                answer[j][i] = matrix[i][j] 
        
        return answer

sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.transpose(matrix))

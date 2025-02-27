# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        
        for i in range(n):
            for j in range(n):
                total_sum += abs(matrix[i][j])
                min_abs_value = min(min_abs_value, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    negative_count += 1
        
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_value
sol=Solution()
matrix = [[1,-1],[-1,1]]
print(sol.maxMatrixSum(matrix))
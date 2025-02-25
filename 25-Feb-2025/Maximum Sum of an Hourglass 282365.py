# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        max_sum = 0
        
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                
                current_sum = (
                    grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j] +  grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] 
                )
          
                max_sum = max(max_sum, current_sum)
        
        return max_sum

sol = Solution()
grid = [[6,2,1,3],
        [4,2,1,5],
        [9,2,8,7],
        [4,1,2,9]]

print(sol.maxSum(grid))  

# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
        
        num_row, num_col = len(mat), len(mat[0])
        diagonals = [[] for _ in range(num_row + num_col - 1)]
        
        for i in range(num_row):
            for j in range(num_col):
                diagonals[i + j].append(mat[i][j])
        
        res = []
        for idx, diagonal in enumerate(diagonals):
            if idx % 2 == 0:
                res.extend(diagonal[::-1])
            else:
                res.extend(diagonal)  
        
        return res

sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.findDiagonalOrder(mat)) 
# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution(object):
    def rotate90(self, mat):
        n = len(mat)
        return [[mat[n - j - 1][i] for j in range(n)] for i in range(n)]

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4):  
            if mat == target:
                return True
            mat = self.rotate90(mat) 
        return False


solution = Solution()
mat = [[0, 1], 
       [1, 0]]

target = [[1, 0], 
          [0, 1]]

print(solution.findRotation(mat, target))  

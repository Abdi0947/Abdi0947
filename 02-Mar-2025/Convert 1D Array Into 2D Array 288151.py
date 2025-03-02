# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m * n:  
            return [] 

        ans = []
        for i in range(m):
            ans.append(original[i * n: (i + 1) * n])  
        return ans

sol = Solution()
original = [1, 2, 3, 4]
m = 2
n = 2
print(sol.construct2DArray(original, m, n))

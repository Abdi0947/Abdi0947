# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
       
        max_count = 0
        max_index = 0
        
        for index, row in enumerate(mat):
            count = row.count(1)
            if count > max_count:
                max_count = count
                max_index = index
        
        return [max_index, max_count]
sol=Solution()
mat = [[0,1],[1,0]]
print(sol.rowAndMaximumOnes(mat))
           

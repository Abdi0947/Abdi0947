# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            row.reverse()  
            for i in range(len(row)):
                row[i] = 1 - row[i]  
        return image
solution=Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
print(solution.flipAndInvertImage(image))
# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

from collections import defaultdict

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        shift_count = defaultdict(int)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x2 - x1, y2 - y1) 
                shift_count[shift] += 1

        return max(shift_count.values() or [0])  

sol = Solution()
img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
print(sol.largestOverlap(img1, img2)) 

# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for i in range(left,right+1):
            isCovered=False
            for start,end in ranges:
                if start<=i<=end:
                    isCovered=True
                    break
            if not isCovered:
                return False
        return True

solution=Solution()
ranges = [[1,10],[10,20]]
left = 21
right = 21
print(solution.isCovered(ranges,left,right))
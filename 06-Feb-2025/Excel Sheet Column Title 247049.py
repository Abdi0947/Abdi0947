# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Handle 1-based indexing
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26
        return ''.join(result[::-1])
solution=Solution()
columnNumber = 1
print(solution.convertToTitle(columnNumber))
        
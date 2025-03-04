# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')
        zeros = s.count('0')
        if ones == 0:
            return s
        elif ones == 1:
            return '0' * zeros + '1'
        else:
            return '1' * (ones - 1) + '0' * zeros + '1'
sol=Solution()
s = "0101"
print(sol.maximumOddBinaryNumber(s))

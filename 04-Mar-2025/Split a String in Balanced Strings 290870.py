# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance=0
        count=0
        for char in s:
            if char=='R':
                balance+=1
            elif char=='L':
                balance-=1
            if balance==0:
                count+=1
        return count
sol=Solution()
s = "RLRRLLRLRL"
print(sol.balancedStringSplit(s))

        
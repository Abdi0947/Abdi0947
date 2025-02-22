# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n)) 
        return n == 1  

sol = Solution()
print(sol.isHappy(19))  
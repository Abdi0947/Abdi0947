# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if (num - 3) % 3 == 0:
            x = (num - 3) // 3
            return [x, x + 1, x + 2]
        
        return []  

solution = Solution()
num = 33
print(solution.sumOfThree(num)) 

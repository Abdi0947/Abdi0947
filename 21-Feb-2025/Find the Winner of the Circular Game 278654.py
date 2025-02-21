# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = list(range(1, n + 1))  
        start = 0 

        while len(nums) > 1: 
            start = (start + k - 1) % len(nums) 
            nums.pop(start) 
        return nums[0]  
sol = Solution()
n = 5
k = 2
print(sol.findTheWinner(n, k))  

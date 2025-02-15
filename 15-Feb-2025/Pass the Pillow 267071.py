# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n, time) :
        position = 1
        direction = 1 
        
        for _ in range(time):
            position += direction
            if position == n or position == 1:
                direction *= -1  
        
        return position

sol = Solution()
print(sol.passThePillow(4, 5))  
print(sol.passThePillow(3, 2)) 

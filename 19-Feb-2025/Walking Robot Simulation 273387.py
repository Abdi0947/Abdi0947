# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands, obstacles):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        directionX = 0
        x, y = 0, 0 
        max_distance = 0 
        obstacle_set = set(map(tuple, obstacles))

        for command in commands: #4 -1
            if command == -1:  
                 directionX = (directionX + 1) % 4 
            elif command == -2:  
                directionX = (directionX - 1) % 4
            else:  
                dx, dy = directions[directionX]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacle_set:
                        break  
                    x += dx  #0+0
                    y += dy  #0+1
                    max_distance = max(max_distance, x**2 + y**2)
        return max_distance
sol = Solution()
print(sol.robotSim([4, -1, 3], []))  
print(sol.robotSim([4, -1, 4, -2, 4], [[2, 4]]))  
print(sol.robotSim([6, -1, -1, 6], [[0, 0]]))  

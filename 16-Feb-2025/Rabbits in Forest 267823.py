# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers) :
        rabbitAnswer = defaultdict(int)
        count = 0
        for answer in answers:
            rabbitAnswer[answer] += 1
        for answer in rabbitAnswer:
           count += (rabbitAnswer[answer] + answer) // (answer + 1) * (answer + 1)
        return count
sol = Solution()
answers = [0, 0, 1, 1, 1]
print(sol.numRabbits(answers))  

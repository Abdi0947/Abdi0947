# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        winner = []
        loser = []
        w = []
        l = []
        result = []
        
        for match in matches:
            winner.append(match[0])
            loser.append(match[1])

        winner_count = Counter(winner)  # {1:2, 3:1, ...}
        loser_count = Counter(loser)  # {3:1, 5:2, ...}
        
        for val, freq in winner_count.items():
            if val not in loser_count:  # If the winner is not in loser_count
                w.append(val)
        
        for val, freq in loser_count.items():
            if freq == 1: 
                l.append(val)
        
        result.append(sorted(w)) 
        result.append(sorted(l))
        return result



solution=Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(solution.findWinners(matches))

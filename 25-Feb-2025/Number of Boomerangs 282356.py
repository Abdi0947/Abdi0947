# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        
        """
        count = 0
        for i in points:
            distance_map = defaultdict(int)
            
            for j in points:
                if i == j:
                    continue
                d = (i[0] - j[0])**2 + (i[1] - j[1])**2
                distance_map[d] += 1
            
            for d in distance_map.values():
                if d > 1:
                    count += d * (d - 1)
        
        return count

sol=Solution()
points = [[0,0],[1,0],[2,0]]
print(sol.numberOfBoomerangs(points))
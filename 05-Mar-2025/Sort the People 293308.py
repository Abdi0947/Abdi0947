# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(heights)
        for i in range(n):
            for j in range(0, n-i-1):
                if heights[j] < heights[j+1]:  
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names
sol=Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sol.sortPeople(names,heights))



        
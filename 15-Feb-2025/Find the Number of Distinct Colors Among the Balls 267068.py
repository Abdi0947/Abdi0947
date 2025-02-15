# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_to_color = {} 
        color_count = {}  
        ans = []

        distinct_colors = 0  

        for ball, color in queries:
            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                if prev_color in color_count:
                    color_count[prev_color] -= 1
                    if color_count[prev_color] == 0:
                        del color_count[prev_color]  
                        distinct_colors -= 1  


            ball_to_color[ball] = color

            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
                distinct_colors += 1  

            ans.append(distinct_colors) 

        return ans
sol = Solution()
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
print(sol.queryResults(4, queries))  # Output: [1, 2, 2, 3]

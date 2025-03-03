# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize min and max with the first array's values
        min_val = arrays[0][0]  
        max_val = arrays[0][-1]  
        result = 0  

        # Iterate through remaining arrays
        for i in range(1, len(arrays)):  
            curr_min = arrays[i][0]  # First element of current array
            curr_max = arrays[i][-1]  # Last element of current array

            # Compute distance from previously seen min/max (ensuring they come from different arrays)
            result = max(result, abs(curr_max - min_val), abs(max_val - curr_min))

            # Update min and max with current array's values
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)

        return result  

# Example usage
sol = Solution()
arrays = [[1,2,3],[4,5],[1,2,3]]
print(sol.maxDistance(arrays)) 

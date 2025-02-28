# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_sum = float('-inf')  
        min_sum = float('inf')   
        current_max = 0         
        current_min = 0         
        
        for num in nums:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)
            
            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)
        
        return max(abs(max_sum), abs(min_sum))
sol = Solution()
nums = [1, -3, 2, 3, -4]
print(sol.maxAbsoluteSum(nums)) 
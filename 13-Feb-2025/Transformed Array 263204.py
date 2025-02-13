# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n 
        for i in range(n):
            if nums[i] > 0:
                new_index = (i + nums[i]) % n  
            elif nums[i] < 0:
                new_index = (i - abs(nums[i])) % n  
            else:
                new_index = i  
            
            result[i] = nums[new_index]  
        
        return result
sol = Solution()
nums = [3, -2, 1, 1]
print(sol.constructTransformedArray(nums))  

nums2 = [-1, 4, -1]
print(sol.constructTransformedArray(nums2)) 

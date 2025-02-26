# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
           return False
    
        
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        mod_map = {0: -1}  
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod = prefix_sum % k
            
            if mod in mod_map:
                if i - mod_map[mod] > 1:
                    return True
            else:
                mod_map[mod] = i
        
        return False
sol=Solution()
nums = [23,2,6,4,7]
k = 13
print(sol.checkSubarraySum(nums,k))
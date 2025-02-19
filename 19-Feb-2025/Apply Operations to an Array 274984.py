# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0 
        index = 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]  
                index += 1  

        return nums
sol = Solution()
nums = [1, 2, 2, 1, 1, 0]
print(sol.applyOperations(nums))  # Output: [1, 4, 1, 0, 0, 0]

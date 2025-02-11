# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        diction = {num: i for i, num in enumerate(nums)}  
        for old, new in operations:
            if old in diction:  
                index = diction[old]
                nums[index] = new  
                diction[new] = index 
                del diction[old]  
        return nums

sol=Solution()
nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]
print(sol.arrayChange(nums,operations))
        
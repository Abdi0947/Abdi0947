# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  
            num_map[num] = i 
        
        return []  


solution = Solution()
nums = [3, 2, 3]
target = 6
print(solution.twoSum(nums, target))  

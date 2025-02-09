# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  
        max_num = nums[-1] 
        total_sum = 0 
        
        for _ in range(k):  
            total_sum += max_num  
            max_num += 1 
        
        return total_sum 

sol = Solution()
nums = [1, 2, 3, 4, 5]
k = 3
print(sol.maximizeSum(nums, k))
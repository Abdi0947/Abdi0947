# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        nums = list(set(nums))  
        nums.sort()  
        longest_streak = 1  
        current_streak = 1 
        for i in range(len(nums)-1):
           
            if nums[i+1]-nums[i]==1:
                current_streak += 1 
            else:
               longest_streak = max(longest_streak,current_streak)
               current_streak = 1 
        return max(longest_streak, current_streak)
sol=Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))
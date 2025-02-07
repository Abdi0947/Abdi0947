# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums) 
        n = len(nums) // 2  
        for num, freq in count.items():
            if freq > n:
                return num  
        
solution = Solution()
nums = [3,2,3]
print(solution.majorityElement(nums))  

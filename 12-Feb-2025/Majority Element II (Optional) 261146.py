# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

from collections import Counter

class Solution:
    def majorityElement(self, nums):
        counter = Counter(nums)
        return [num for num, frequency in counter.items() if frequency > len(nums) // 3]
        
solution = Solution()
nums = [3, 2, 3]
print(solution.majorityElement(nums))

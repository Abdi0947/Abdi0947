# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)
sol=Solution()
nums = [5,2,3,1]
print(sol.sortArray(nums))
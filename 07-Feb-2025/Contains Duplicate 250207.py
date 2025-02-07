# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=Counter(nums)
        for freq in count.values():
            if freq > 1:
                return True
        return False
solution=Solution()
nums = [1,2,3,1]
print(solution.containsDuplicate(nums))
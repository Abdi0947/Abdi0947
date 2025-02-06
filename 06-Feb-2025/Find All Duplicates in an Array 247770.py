# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=Counter(nums)
        duplicates=[num for num,freq in count.items()  if freq>1]
        return(duplicates)
solution=Solution()
nums = [4,3,2,7,8,2,3,1]
print(solution.findDuplicates(nums))
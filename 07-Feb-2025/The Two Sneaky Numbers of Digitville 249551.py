# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=Counter(nums)
        val=[num for num,freq in count.items()if freq>=2]
        return val
solution=Solution()
nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(solution.getSneakyNumbers(nums))
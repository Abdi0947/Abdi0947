# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=Counter(nums)
        pairs=0
        leftover=0
        for freq in count.values():
            pairs += freq // 2   
            leftover += freq % 2  
        return [pairs,leftover]
solution=Solution()
nums = [1,3,2,1,3,2,2]
print(solution.numberOfPairs(nums))
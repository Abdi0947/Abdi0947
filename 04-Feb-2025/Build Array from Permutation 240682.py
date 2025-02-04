# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))] 
solution=Solution()
nums = [0,2,1,5,3,4]
print(solution.buildArray(nums))
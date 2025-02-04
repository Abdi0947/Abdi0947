# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return(max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1]))
       
    
solution=Solution()
nums = [1,2,3]
nums1=[-100,-98,-1,2,3,4] #39200
print(solution.maximumProduct(nums))
# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_map = {0: -1}
        max_len = 0
        cumulative_sum = 0
    
        for i in range(len(nums)):
            if nums[i] == 0:
                cumulative_sum -= 1
            else:
                cumulative_sum += 1
            
            if cumulative_sum in sum_map:
                max_len = max(max_len, i - sum_map[cumulative_sum])
            else:
                sum_map[cumulative_sum] = i
        
        return max_len
sol=Solution()
nums = [0,1]
print(sol.findMaxLength(nums))
        
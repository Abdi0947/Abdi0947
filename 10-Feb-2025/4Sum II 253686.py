# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0
        sum_map = defaultdict(int) 
        
        for num1 in nums1:
            for num2 in nums2:
                sum_map[num1 + num2] += 1
        
    
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)  
                if target in sum_map:
                    count += sum_map[target]  
        
        return count

sol = Solution()
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(sol.fourSumCount(nums1, nums2, nums3, nums4))

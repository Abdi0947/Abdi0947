# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg=[]
        pos=[]
        all=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(pos)):
            all.append(pos[i])
            all.append(neg[i])
        return all
solution=Solution()
nums = [3,1,-2,-5,2,-4]
print(solution.rearrangeArray(nums))
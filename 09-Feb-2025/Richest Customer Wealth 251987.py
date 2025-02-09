# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        arr=[]
        total=0
        for num in accounts:
            for val in num:
                total+=val
            arr.append(total)
            total=0
        return max(arr)

sol=Solution()
accounts = [[1,2,3],[3,2,1]]
print(sol.maximumWealth(accounts))
# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a=set(a)
        b=set(b)
        
        a = set(a)
        b = set(b)
        
        # Check if b is a subset of a
        if b.issubset(a):
            return "true"
        else:
            return "false"
    

sol=Solution()
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
print(sol.isSubset(a,b))
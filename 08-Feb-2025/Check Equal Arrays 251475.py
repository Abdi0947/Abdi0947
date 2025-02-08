# Problem: Check Equal Arrays - https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        return "true" if sorted(a) == sorted(b) else "false"
sol=Solution()
a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]
print(sol.checkEqual(a,b))

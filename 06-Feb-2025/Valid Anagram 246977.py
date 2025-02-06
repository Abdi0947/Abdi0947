# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)
solution=Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s,t))
# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        found=False
        w=[]
        for ch in words:
            for word in ch:
                if word in allowed:
                    found=True
                else:
                    found = False
                    break
            if found:
                w.append(word)
        return len(w)
solution=Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(solution.countConsistentStrings(allowed,words))
# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n=len(s)
        shufeled=['']*n
        for i, val in enumerate(indices):
            shufeled[val] = s[i]
        return ''.join(shufeled)

solution=Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(solution.restoreString(s,indices))
# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        length=len(s)
        occ=s.count(letter)
        return (occ*100)/length
solution=Solution()
s = "kue"
letter = "e"
print(solution.percentageLetter(s,letter))
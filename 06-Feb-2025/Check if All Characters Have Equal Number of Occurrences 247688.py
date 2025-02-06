# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        occ_count = Counter(s)  
        freq_values = set(occ_count.values())
        return len(freq_values) == 1

solution = Solution()
s = "abacbc"
print(solution.areOccurrencesEqual(s))
# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        letter_count = Counter(s)

        sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))

        sorted_result = ''.join([letter * count for letter, count in sorted_letters])
        return sorted_result
sol=Solution()
s = "tree"
print(sol.frequencySort(s))
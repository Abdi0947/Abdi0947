# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

from collections import defaultdict

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lookup = defaultdict(set)
        for word in words:
            lookup[word] = set(word)

        def have_no_common(i, j):
            return not (lookup[i] & lookup[j])  

        mx = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if have_no_common(words[i], words[j]):
                    mx = max(mx, len(words[i]) * len(words[j]))

        return mx

sol = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(sol.maxProduct(words))  

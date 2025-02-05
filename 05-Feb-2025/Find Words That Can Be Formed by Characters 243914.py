# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charss=Counter(chars)
        length=0
        for word in words:
            word_count=Counter(word)
            if all(word_count[ch]<=charss[ch] for ch in word):
                length+=len(word)
        return length
solution=Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(solution.countCharacters(words,chars))
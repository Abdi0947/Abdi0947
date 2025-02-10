# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        
        for word in strs:
            count = tuple(sorted(Counter(word).items()))  # Frequency count as key
            anagram_map[count].append(word)
        
        return list(anagram_map.values())
        
sol=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))
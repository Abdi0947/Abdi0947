# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False  

        mapping_s_t = {}  # Mapping from s -> t
        mapping_t_s = {}  # Mapping from t -> s

        for char_s, char_t in zip(s, t):
            
            if (char_s in mapping_s_t and mapping_s_t[char_s] != char_t) or \
               (char_t in mapping_t_s and mapping_t_s[char_t] != char_s):
                return False
            mapping_s_t[char_s] = char_t
            mapping_t_s[char_t] = char_s

        return True 
sol = Solution()
print(sol.isIsomorphic("paper", "title"))
print(sol.isIsomorphic("foo", "bar"))     
print(sol.isIsomorphic("egg", "add"))    
print(sol.isIsomorphic("badc", "baba"))   

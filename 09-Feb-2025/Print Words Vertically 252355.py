# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution(object):
    def printVertically(self, s):
        ver = []  
        m = s.split()
        max_len = max(len(word) for word in m)  # Fix: Find the longest word's length

        for i in range(max_len):
            vertical_word = [] 

            for word in m:
                if i < len(word):
                    vertical_word.append(word[i])  
                else:
                    vertical_word.append(' ')  # Padding spaces for shorter words
            
            ver.append(''.join(vertical_word).rstrip())  # Remove trailing spaces
        
        return ver  

# Example Usage
solution = Solution()
s = "HOW ARE YOU"
print(solution.printVertically(s))

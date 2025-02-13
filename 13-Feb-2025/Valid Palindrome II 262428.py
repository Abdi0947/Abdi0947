# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        
        return True  # If the entire string is a palindrome

# Testing the function
sol = Solution()
s = 'aba'
print(sol.validPalindrome(s))  # Output: True

s = 'abca'
print(sol.validPalindrome(s))  # Output: True

s = 'abcdef'
print(sol.validPalindrome(s))  # Output: False

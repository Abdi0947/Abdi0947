# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

import re

class Solution(object):
    def maskPII(self, s):
        if '@' in s:  # Email case
            name, domain = s.split('@')
            masked_name = name[0].lower() + "*****" + name[-1].lower()
            return masked_name + "@" + domain.lower()
        
        else:  # Phone number case
            digits = re.sub(r'\D', '', s)  # Remove all non-digit characters
            local_number = digits[-10:]  # Last 10 digits
            country_code = digits[:-10]  # Digits before last 10
            
            # Create masked format based on country code length
            masked_number = "***-***-" + local_number[-4:]
            if country_code:
                masked_number = "+" + "*" * len(country_code) + "-" + masked_number
            
            return masked_number

# Example usage
solution = Solution()
print(solution.maskPII("LeetCode@LeetCode.com"))  # Output: "l*****e@leetcode.com"
print(solution.maskPII("1(234)567-890"))         # Output: "***-***-7890"
print(solution.maskPII("+1-800-555-1234"))       # Output: "+*-***-***-1234"

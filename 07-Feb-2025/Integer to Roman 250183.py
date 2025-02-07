# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman = ""
        for value,symbol in values:
             while num >= value:
                roman += symbol  
                num -= value  
        return roman
solution=Solution()
num = 3749
print(solution.intToRoman(num))
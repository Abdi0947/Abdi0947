# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res, buffer, isOpen = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                # Single-line comment (//)
                if i < len(line) - 1 and line[i] == '/' and line[i + 1] == '/' and not isOpen:
                    break
                
                # Start of block comment (/*)
                elif i < len(line) - 1 and line[i] == '/' and line[i + 1] == '*' and not isOpen:
                    isOpen = True
                    i += 1  # Skip the '*'
                
                # End of block comment (*/)
                elif i < len(line) - 1 and line[i] == '*' and line[i + 1] == '/' and isOpen:
                    isOpen = False
                    i += 1  # Skip the '/'
                
                # Add valid code to buffer
                elif not isOpen:
                    buffer += line[i]
                
                i += 1
            
            # Append buffer to result if valid code exists and we're outside a block comment
            if buffer and not isOpen:
                res.append(buffer)
                buffer = ""  # Clear buffer for the next line
        
        return res

# Test case
solution = Solution()
source = [
    "/*Test program */", 
    "int main()", 
    "{ ", 
    "  // variable declaration ", 
    "int a, b, c;", 
    "/* This is a test", 
    "   multiline  ", 
    "   comment for ", 
    "   testing */", 
    "a = b + c;", 
    "}"
]
print(solution.removeComments(source))

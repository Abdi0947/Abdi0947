# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0  
        
        for op in operations: 
            if op in ("++X", "X++"):  
                X += 1  
            elif op in ("--X", "X--"):
                X -= 1 
        
        return X 

solution = Solution()
operations = ["++X", "++X", "X++"]
print(solution.finalValueAfterOperations(operations)) 
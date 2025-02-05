# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        # Initialize the sum of even numbers in the list
        even_total = sum(num for num in nums if num % 2 == 0)
        
        # Process each query
        for val, index in queries:
            old_value = nums[index]  # Get the old value before updating
            
            # Remove old_value from even_total if it was even
            if old_value % 2 == 0:
                even_total -= old_value
            
            # Apply the query: Update the number at the given index
            nums[index] += val
            
            # Add the updated number to even_total if it's even
            if nums[index] % 2 == 0:
                even_total += nums[index]
            
            # Append the current sum of even numbers to result
            result.append(even_total)
        
        return result

# Example usage
solution = Solution()
nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(solution.sumEvenAfterQueries(nums, queries))  # Expected Output: [8, 6, 4, 10]

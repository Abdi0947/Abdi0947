# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_index = {}  
        min_sum = float('inf') 
        for index, word in enumerate(list1):
            if word in list2:
                index_of_1 = index
                index_of_2 = list2.index(word)
                s = index_of_1 + index_of_2

                if s < min_sum:
                    min_sum = s  
                    min_index[min_sum] = [word] 
                elif s == min_sum:
                    min_index[min_sum].append(word)  

        return min_index[min_sum] 
solution = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(solution.findRestaurant(list1, list2))  

# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet(object):

    def __init__(self):
        """Initialize data structures to store unique values."""
        self.data_set = set()  # Set for fast lookup
        self.data_list = []    # List for random access

    def insert(self, val):
        """
        Inserts a value. Returns True if the value was not present.
        :type val: int
        :rtype: bool
        """
        if val not in self.data_set:
            self.data_set.add(val)
            self.data_list.append(val)
            return True 
        return False  

    def remove(self, val):
        """
        Removes a value. Returns True if the value was present.
        :type val: int
        :rtype: bool
        """
        if val in self.data_set:
            self.data_set.remove(val)
            self.data_list.remove(val)  
            return True 
        return False  

    def getRandom(self):
        """
        Returns a random element from the set.
        :rtype: int
        """
        if not self.data_list:
            return None  
        return random.choice(self.data_list)  


obj = RandomizedSet()
print(obj.insert(1))  
print(obj.insert(2))   
print(obj.insert(2)) 
print(obj.remove(1))   
print(obj.getRandom())

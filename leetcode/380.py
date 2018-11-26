"""
Author:  ZHAO Zinan
Created: 26-Nov-2018

380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.sample(self.data, 1)[0]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# test
if __name__ == '__main__':
    randomset = RandomizedSet()
    print(randomset.insert(0)) # true
    print(randomset.insert(1)) # true
    print(randomset.insert(0)) # false
    print(randomset.insert(2)) # true
    print(randomset.remove(0)) # true
    print(randomset.remove(0)) # false
    print(randomset.getRandom()) # 1 or 2
'''
Author:    ZHAO Zinan
Created: 29-Oct-2018

729. My Calendar I
https://leetcode.com/problems/my-calendar-i/description/
'''
class IntervalTreeNode:
    def __init__(self, interval=[]):
        self.left = []
        self.right = []
        self.interval = interval

    def overlap(self, anotherInterval):
        if anotherInterval[0] >= self.interval[1]:
            return False if not self.right else self.right.overlap(anotherInterval)
        if anotherInterval[1] <= self.interval[0]:
            return False if not self.left else self.left.overlap(anotherInterval)
        return True

    # assume no overlap in the tree
    def insert(self, anotherInterval):
        if self.interval == []:
            self.interval = anotherInterval
            return True
        if anotherInterval[0] >= self.interval[1]:
            if self.right:
                self.right.insert(anotherInterval)
                return True
            else:
                self.right = IntervalTreeNode(anotherInterval)
                return True

        if anotherInterval[1] <= self.interval[0]:
            if self.left:
                self.left.insert(anotherInterval)
                return True
            else:
                self.left = IntervalTreeNode(anotherInterval)
                return True
        return False

class MyCalendar:

    def __init__(self):
        self.root = IntervalTreeNode()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        interval = [start, end]
        if self.root.interval == [] or not self.root.overlap(interval):
            self.root.insert(interval)
            return True
        
        return False
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# test
if __name__== '__main__':
    obj = MyCalendar()
    print(obj.book(10, 20)) # True
    print(obj.book(15, 25)) # False
    print(obj.book(20, 30)) # True

'''
Author:    ZHAO Zinan
Created: 29-Oct-2018

729. My Calendar II
https://leetcode.com/problems/my-calendar-ii/description/
'''
class IntervalTreeNode:
    def __init__(self, interval=[]):
        self.left = []
        self.right = []
        self.interval = interval
        self.max = interval[1] if interval else 0

    def overlap(self, anotherInterval):
        if anotherInterval[0] >= self.interval[1]:
            return False if not self.right else self.right.overlap(anotherInterval)
        if anotherInterval[1] <= self.interval[0]:
            return False if not self.left else self.left.overlap(anotherInterval)
        return True

    def overlapTwice(self, anotherInterval):
        if anotherInterval

    # assume no overlap in the tree
    def insert(self, anotherInterval):
        if self.interval == []:
            self.interval = anotherInterval
            self.max = anotherInterval[1]
            return True

        self.max = max(self.max, anotherInterval[1])
        if anotherInterval[0] >= self.interval[0]:
            if self.right:
                self.right.insert(anotherInterval)
                return True
            else:
                self.right = IntervalTreeNode(anotherInterval)
                return True

        elif anotherInterval[0] < self.interval[0]:
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
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
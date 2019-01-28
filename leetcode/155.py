'''
Author:    ZHAO Zinan
Created: 01/27/2019

155. Min Stack
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nodes = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[len(self.min)-1]))
        self.nodes.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.min.pop()
        self.nodes.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.nodes[len(self.nodes)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[len(self.min)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
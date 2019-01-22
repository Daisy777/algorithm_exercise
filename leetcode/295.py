'''
Author:    ZHAO Zinan
Created: 01/21/2019

295. Find Median from Data Stream
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nodes = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.nodes) == 0:
            self.nodes.append(num)
            return
        if num <= self.nodes[0]:
            self.nodes.insert(0,  num)
            return 

        if num >= self.nodes[len(self.nodes)-1]:
            self.nodes.append(num)
            return 

        i = 0
        j = len(self.nodes)

        # binary search
        while(i<j):
            if i == j-1:
                self.nodes.insert(j, num)
                return 
            middle = (i+j)//2
            if self.nodes[middle] == num:
                self.nodes.insert(middle, num)
                return
            elif self.nodes[middle] < num:
                i = middle
            else:
                j = middle
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nodes)
        if n == 0:
            return 0
        if n&1:
            return self.nodes[n//2]
        else:
            return (self.nodes[n//2-1]+self.nodes[n//2])/2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# test
if __name__ == '__main__':
    # # test 1
    # obj = MedianFinder()
    # obj.addNum(1)
    # obj.addNum(2)
    # print(obj.findMedian()) # 1.5
    # obj.addNum(3)
    # print(obj.findMedian()) # 2

    # # test 2
    # obj = MedianFinder()
    # obj.addNum(-1)
    # print(obj.findMedian()) # -1
    # obj.addNum(-2)
    # print(obj.findMedian()) # -1.5
    # obj.addNum(-3)
    # print(obj.findMedian()) # -2
    # obj.addNum(-4)
    # print(obj.findMedian()) # -2.5
    # obj.addNum(-5)
    # print(obj.findMedian()) # -3

    # test 3
    obj = MedianFinder()
    obj.addNum(6)
    obj.addNum(10)
    obj.addNum(2)
    obj.addNum(6)
    obj.addNum(5)
    obj.addNum(0)
    obj.addNum(6)
    obj.addNum(3)
    obj.addNum(1)
    obj.addNum(0)
    obj.addNum(0)
    print(obj.findMedian())



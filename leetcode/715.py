'''
Author:    ZHAO Zinan
Created: 06-Nov-2018

715. Range Module
https://leetcode.com/problems/range-module/description/
'''
class RangeModule:
    # complete tree
    def __init__(self):
        self.intervals = []
        
    def _findele(self, ele):
        if len(self.intervals) > 0:
            if ele < self.intervals[0]:
                return 0
            elif ele >= self.intervals[len(self.intervals)-1]:
                return len(self.intervals)
            else:
                begin = 0
                end = len(self.intervals)-1

                while True:    
                    middle = (begin+end)//2
                    
                    if end - begin == 1:
                        return end
                    
                    if self.intervals[middle] == ele:
                        return middle
                    elif self.intervals[middle] > ele:
                        end = middle
                    elif self.intervals[middle] < ele:
                        begin = middle

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if len(self.intervals) == 0:
            self.intervals.extend([left, right])
            return
        
        left_index = self._findele(left)
        right_index = self._findele(right)
        
        if not right_index & 1:
            self.intervals.insert(right_index, right)
            right_index -= 1
        if not left_index & 1:
            self.intervals.insert(left_index, left)
            left_index += 1
            right_index += 1
        
        self.intervals = [value for index, value in enumerate(self.intervals) if index > right_index or index < left_index]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        left_index = self._findele(left)
        right_index = self._findele(right)
        if left_index != right_index and self.intervals[left_index] == left and not left_index & 1:
            return True

        if left_index != right_index or not left_index & 1:
            return False
        return True

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        left_index = self._findele(left)
        right_index = self._findele(right)

        if left_index == right_index:
            if left_index & 1:
                self.intervals.insert(left_index, left)
                self.intervals.insert(left_index+1, right)
            return 
        
        if left_index & 1:
            self.intervals.insert(left_index, left)
            left_index += 1
        if right_index & 1:
            self.intervals.insert(right_index, right)
            
        self.intervals = [value for index, value in enumerate(self.intervals) if index >= left_index and index <= right_index]
        

# test 
if __name__ == '__main__':
    # rangemodule = RangeModule()
    # rangemodule.addRange(10, 20)
    # rangemodule.removeRange(14, 16)
    # print(rangemodule.intervals)
    # print(rangemodule.queryRange(10, 14)) # true
    # print(rangemodule.queryRange(13, 15)) # false
    # print(rangemodule.queryRange(16, 17)) # true

    rangemodule = RangeModule()
    rangemodule.addRange(10, 180)
    rangemodule.addRange(150, 200)
    rangemodule.addRange(250, 500)
    print(rangemodule.intervals)
    print(rangemodule.queryRange(50, 100)) # true
    print(rangemodule.queryRange(180, 300)) # false
    print(rangemodule.queryRange(600, 1000)) # false
    rangemodule.removeRange(50, 150)
    print(rangemodule.intervals)
    print(rangemodule.queryRange(50, 100)) # false



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
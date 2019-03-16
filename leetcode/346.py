class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.valnum = 0
        self.p = 0
        self.arr = [0]*size
        self.size = size

    def next(self, val: int) -> float:
        self.arr[self.p%self.size] = val
        self.p+=1
        self.valnum += 1
        if self.valnum >= self.size:
            return sum(self.arr)/self.size
        return sum(self.arr)/self.valnum


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
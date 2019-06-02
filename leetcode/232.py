'''
Author:    ZHAO Zinan
Created: 02-Jun-2019

232. Implement Queue using Stacks
'''
# use list as a stack here
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.ele = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # put the ele to the first place of the stack
        templist = [0]*(self.ele)
        
        i = 1
        while(i <= self.ele):
            templist[-i] = self.stack.pop() 
            i += 1
        self.stack.append(x) 
        
        
        i=0
        while(i < self.ele):
            self.stack.append(templist[i])
            i+= 1
        self.ele += 1
        
            
        
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        assert(self.ele != 0)
        self.ele -= 1
        return self.stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.ele == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
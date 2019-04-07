'''
Author: ZHAO Zinan
Created: 07. April 2019

706. Design HashMap
''' 
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 100000
        self.arr = [None]*self.len

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        locArr = key%self.len
        if self.arr[locArr] == None:
            self.arr[locArr] = Node(key, value)
        else:
            ptr = self.arr[locArr]
            complete = False
            while(ptr.next!=None and not complete):
                if ptr.key != key:
                    ptr = ptr.next
                else:
                    ptr.val = value
                    complete = True
            if ptr.key == key:
                ptr.val = value
                complete = True
            if not complete: ptr.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        locArr = key%self.len
        if self.arr[locArr] == None:
            return -1
        ptr = self.arr[locArr]
        while(ptr.next!=None):
            if ptr.key == key:
                return ptr.val
            ptr = ptr.next
        if ptr.key == key:
                return ptr.val
        else: return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        locArr = key%self.len
        if self.arr[locArr] == None:
            return
        ptr = self.arr[locArr]
        if ptr.key == key:
            self.arr[locArr] = ptr.next
        while(ptr.next != None):
            if ptr.next.key == key:
                # we should remove ptr.next node
                ptr.next = ptr.next.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
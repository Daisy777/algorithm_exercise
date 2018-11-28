'''
Author:    ZHAO Zinan
Created: 11/27/2018

146. LRU Cache
https://leetcode.com/problems/lru-cache/description/

linked list queue and dictionary
'''
class LinkedNode:
    def __init__(self, value):
        self.pre = None
        self.next = None
        self.value = value

    def insertAfter(self, node):
        node.pre = self
        node.next = self.next

        if self.next:
            self.next.pre = node
        
        self.next = node

    def insertBefore(self, node):
        node.pre = self.pre
        node.next = self

        if self.pre:
            self.pre.next = node

        self.pre = node

    def removeNode(self):
        if self.pre:
            self.pre.next = self.next
        if self.next:
            self.next.pre = self.pre

        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.mostRecent = None
        self.leastRecent = None
        self.hash = {}           # used to record location of node in linkedlist

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            location = self.hash[key]
            # move the linkedlistnode to the mostRecent side
            if location != self.mostRecent:
                if location == self.leastRecent:
                    self.leastRecent = self.leastRecent.pre
                location.removeNode()
                self.mostRecent.insertBefore(location)
                self.mostRecent = self.mostRecent.pre

            return location.value

        return -1

    def put(self, key, value):
        """
        put the newly arrived to most recently side

        :type key: int
        :type value: int
        :rtype: void
        """
        # update if it already exists
        if key in self.hash and self.hash[key] != -1:
            node = self.hash[key]
            node.value = value

            if node != self.mostRecent:
                if node == self.leastRecent:
                    self.leastRecent = node.pre
                node.removeNode()

                # put it to the most recently used side
                self.mostRecent.insertBefore(node)
                self.mostRecent = self.mostRecent.pre
            
            return 

        node = LinkedNode(value)

        if self.capacity > self.size:
            if self.mostRecent:
                self.mostRecent.insertBefore(node) 
                self.mostRecent = self.mostRecent.pre
            else:
                if not self.leastRecent:
                    self.leastRecent = node
                self.mostRecent = node
            self.size += 1
        else:
            # instead of remove it from hash table, change value to -1
            self.leastRecent.value = -1
            # the new node replaces self.leaseRecent
            self.mostRecent.insertBefore(node)
            self.mostRecent = self.mostRecent.pre
            self.leastRecent = self.leastRecent.pre
            
        self.hash[key] = self.mostRecent
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
Author:    ZHAO Zinan
Created: 12/07/2018

547. Friend Circles
https://leetcode.com/problems/friend-circles/description/
'''
class disjointSet:
    def __init__(self, length):
        self.leaders = [-1] * length
        self.length = length

    def size(self):
        sizeLeaders = 0
        for index, val in enumerate(self.leaders):
            if val < 0:
                sizeLeaders += 1
        return sizeLeaders

    def root(self, index):
        if index > self.length -1 or index < 0:
            return -1 # invalid parameter
        if self.leaders[index] < 0:
            return index

        return self.root(self.leaders[index]) # O(logn)

    def combine(self, index1, index2):
        # add the set with smaller depth as the child of the other ones
        root1 = self.root(index1) 
        root2 = self.root(index2)
        if root1 == -1 or root2 == -1:
            return False # invalid

        if root1 == root2:
            return True # already in the same set
        
        if -self.leaders[root1] > -self.leaders[root2]:
            parent = root1
            child = root2
        else:
            parent = root2
            child = root1

        self.leaders[parent] = min(self.leaders[parent], self.leaders[child]-1)
        self.leaders[child] = parent
        return True # success

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # disjoint set
        number = len(M)
        if not number:
            return 0
        
        friendship = disjointSet(number)
        for i in range(number):
            for j in range(i+1, number):
                if M[i][j]:
                    friendship.combine(i, j)
        
        return friendship.size()


# test
if __name__ == '__main__':
    test1 = [[1,1,0],
            [1,1,0],
            [0,0,1]]
    print(Solution().findCircleNum(test1)) # 2

    test2 = [[1,1,0],
            [1,1,1],
            [0,1,1]]
    print(Solution().findCircleNum(test2)) # 1

    test3 = [[1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]]
    print(Solution().findCircleNum(test3)) # 1

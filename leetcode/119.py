'''
Author:    ZHAO Zinan
Created: 02-Nov-2018

119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/description/
'''
class Solution:
    def combination(self, rowIndex, col):
        return self.factorial(rowIndex-col+1, rowIndex)//self.factorial(1, col)
    
    def factorial(self, begin, end):
        mul = 1
        for i in range(begin, end+1):
            mul *= i
            
        return mul
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        elements = []
        for i in range(rowIndex+1):
            elements.append(self.combination(rowIndex, i))
        return elements
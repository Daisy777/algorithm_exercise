'''
Author: ZHAO Zinan
Created: 28. April 2019

1033. Moving Stones Until Consecutive
''' 
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x = min(a, b, c) 
        z = max(a, b, c) 
        y = a+b+c-x-z 

        if x == y-1 and z == y+1:
            return [0, 0]

        nummax = z-y-1 + y-x-1
        nummin = 1 if x == y-2 or z == y+2 or z == y+1 or x == y-1 else 2
        return [nummin, nummax]
        
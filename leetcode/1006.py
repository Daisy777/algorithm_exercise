'''
Author: ZHAO Zinan
Created: 10. March 2019

1006. Clumsy Factorial
''' 

# reminder: // in python is not floor division??
class Solution:
    def clumsy(self, N: int) -> int:
        import math
        sumclumsy = 0
        i = 1
        while(N):
            if N//4 > 0:
                sumclumsy += i*math.floor(N*(N-1)/(N-2))+(N-3)
                N -= 4
                i = -1
    
            elif N//3 > 0:
                sumclumsy += i*N*(N-1)//(N-2)
                return sumclumsy
            elif N//2 > 0:
                sumclumsy += i*N*(N-1)
                print(sumclumsy)
                return sumclumsy
            else:
                sumclumsy += i*N
                return sumclumsy
            
        return sumclumsy
            
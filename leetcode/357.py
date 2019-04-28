'''
Author: ZHAO Zinan
Created: 26. April 2019

357. Count Numbers with Unique Digits
''' 
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n > 10:
            return 0
        digit = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        answer = 1
        product = 1
        
        
        for i in range(n):
            product *= digit[i]
            answer += product
            

        return answer
        
        


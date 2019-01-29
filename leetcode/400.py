'''
Author:    ZHAO Zinan
Created: 01/29/2019

400. Nth Digit
'''
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        sum = 0
        if n > 0 and n < 10:
            return n

        while (True):
            if n > sum and n <= sum+9*10**(digit-1)*digit:
                period_num = (n-sum-1)//digit
                num_within_period = (n-sum-1)%digit
                # print(sum, digit,period_num, num_within_period)
                # print(str(10**(digit-1)+period_num))
                return int(str(10**(digit-1)+period_num)[num_within_period])
            sum += 9*10**(digit-1)*digit
            digit += 1
            

# test
if __name__ == '__main__':
    print(Solution().findNthDigit(3)) # 3
    print(Solution().findNthDigit(11)) # 0
    print(Solution().findNthDigit(10)) # 1
    print(Solution().findNthDigit(12)) # 1
    print(Solution().findNthDigit(190)) # 1

    print(Solution().findNthDigit(1000)) # 3
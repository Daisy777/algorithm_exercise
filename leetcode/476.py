'''Author:    ZHAO Zinan
Created: 12/08/2018

476. Number Complement
https://leetcode.com/problems/number-complement/description/
'''
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i < num:
            i = (i << 1) + 1

        return i ^ num

# test
if __name__ == '__main__':
    print(Solution().findComplement(5)) # 2
    print(Solution().findComplement(1)) # 0
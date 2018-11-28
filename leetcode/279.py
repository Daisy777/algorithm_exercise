'''
Author:    ZHAO Zinan
Created: 11/27/2018

279. Perfect Squares
https://leetcode.com/problems/perfect-squares/description/
'''
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # base case 
        if n == 0:
            return 0
        if n < 0:
            return float('inf')
        if n == 1:
            return 1
    
        largest_division = math.floor(math.sqrt(n))
        if (largest_division*largest_division == n):
            return 1

        min_times = float('inf')
        for i in range(largest_division+1, largest_division//2, -1):
            min_times = min(min_times, self.numSquares(n-i*i)+1)
            if min_times == 1:
                return 1

        return min_times


# test 
if __name__ == '__main__':
    print(Solution().numSquares(13)) # 2 (4+9)
    print(Solution().numSquares(12)) # 3 (4+4+4)

        
        
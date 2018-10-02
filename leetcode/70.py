class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            x = 1
            y = 2

            for i in range(n-2):
                result = x + y
                x = y
                y = result

            return result
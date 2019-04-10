'''
Author: ZHAO Zinan
Created: 10. April 2019

216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.
''' 
class Solution:
    def combinationSum3(self, k, n):
        def _combination(k, n, range):
            if k == 0 and n!=0:
                return False

            if k == 1 and n in range:
                return [[n]]

            result = []
            for index, i in enumerate(range):
                recursion = _combination(k-1, n-i, range[index+1:])
                if recursion != False:
                    result.extend([[i]+r for r in recursion])
            return result
                
        return _combination(k, n, list(range(1, 10)))

# test
if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))
    print(Solution().combinationSum3(3, 9))

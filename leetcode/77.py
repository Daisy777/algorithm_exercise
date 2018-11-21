'''
Author:    ZHAO Zinan
Created: 21-Nov-2018

77. Combinations
https://leetcode.com/problems/combinations/description/
'''
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]

        if k == n:
            return [list(range(1, n+1))]

        # the result that don't contain the last element
        result = self.combine(n-1, k)
        # the result that contains the last element
        result1 = self.combine(n-1, k-1)
        result.extend([x+[n] for x in result1])

        return result






# test
import unittest

class TestCombination(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testCombine(self):
        self.assertEqual(self.solution.combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
        
if __name__ == '__main__':
    unittest.main()
'''
Author:    ZHAO Zinan
Created: 07-Nov-2018

22. Generate Parenthesis
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._generateParenthesis('', n, n, n)
        return self.list
        
        
    def _generateParenthesis(self, string, left, right, n):
        if len(string) >= n*2:
            self.list.append(string)

        if left:
            self._generateParenthesis(string+'(', left-1, right, n)
        if right > left:
            self._generateParenthesis(string+')', left, right-1, n)

# test
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
    print(len(solution.generateParenthesis(4))) # 14

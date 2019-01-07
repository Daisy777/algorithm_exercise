'''
Author:    ZHAO Zinan
Created: 01/07/2019

17. Letter Combinations of a Phone Number
'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }

        result = []
        if len(digits) == 1:
            return [x for x in mapping[digits[0]]]

        digit = digits[0]
        digits = digits[1:]
        mapped_letters = mapping[digit]
        result.extend([mapped_letter + x for x in self.letterCombinations(digits) for mapped_letter in mapped_letters] )
        
        return result

# test
if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
    # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


'''
Author: ZHAO Zinan
Created: 04. April 2019

784. Letter Case Permutation
     Given a string S, we can transform every letter individually to be
     lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
''' 
class Solution:
    def letterCasePermutation(self, S: str):
        # recursion
        if not S:
            return ['']

        first = S[0]
        if first.islower():
            return [first+i for i in self.letterCasePermutation(S[1:])]+[first.upper()+i for i in self.letterCasePermutation(S[1:])]
        elif first.isupper():
            return [first+i for i in self.letterCasePermutation(S[1:])]+[first.lower()+i for i in self.letterCasePermutation(S[1:])]
        else:
            return [first+i for i in self.letterCasePermutation(S[1:])]

# test
if __name__ == '__main__':
    print(Solution().letterCasePermutation("a1b2"))
    print(Solution().letterCasePermutation("3z4"))
    print(Solution().letterCasePermutation("12345"))
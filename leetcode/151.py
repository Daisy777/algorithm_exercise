'''Author: ZHAO Zinan
Created: 28. February 2019

151. Reverse Words in a String
not a good algorithm problem for python users...
''' 
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
'''
Author:    ZHAO Zinan
Created: 12/14/2018

5. Longest Palindromic Substring
'''
class Solution:
    def centralFussion(self, s, start, end):
        while (start >= 0 and end < len(s) and s[start] == s[end]):
            start -= 1
            end += 1
            
        # as there is one more -= 1 and += 1
        if end - start - 1 > self.maxLen:
            self.maxLen = end-start-1
            self.begin = start+1
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxLen = 1
        self.begin = 0
        
        for i in range(len(s)):
            self.centralFussion(s, i, i) # odd length palindromic
        
        for i in range(len(s)-1):
            self.centralFussion(s, i, i+1) # even length palindramic
            
        return s[self.begin: self.begin+self.maxLen]
           
        
# test
if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd")) # bb
    print(Solution().longestPalindrome("babad")) # bab
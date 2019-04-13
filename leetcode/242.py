'''
Author: ZHAO Zinan
Created: 13. April 2019

242. Valid Anagram
''' 
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        if counter1 == counter2:
            return True
        return False
    
'''
faster solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(c) == t.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')
'''
# test
if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
    print(Solution().isAnagram("cat", "rat"))
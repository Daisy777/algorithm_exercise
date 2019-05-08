'''
Author:    ZHAO Zinan
Created: 08-May-2019



Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
from typing import List 
import collections 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countlist = []
        result = []
        for str in strs:
            count = collections.Counter(str)
            if count in countlist:
                result[countlist.index(count)].append(str) 
            else:
                countlist.append(count)
                result.append([])
                result[-1].append(str) 
        return result 

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))
    
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mem = {}
        
        for s in strs:
            std = ''.join(sorted(s))
            if std in mem:
                mem[std] += [s]
            else:
                mem[std] = [s]
        return list(mem.values())
'''
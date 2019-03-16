# not only a-z A-Z but also some special characters
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        remaining = 1 if len(s)&1 else 0
        
        from collections import defaultdict
        
        dic = defaultdict(int)
        for char in s:
            dic[char] ^= 1
            
        sumdict = 0
        for key in dic:
            sumdict += dic[key]
            
        return sumdict == remaining
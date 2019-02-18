class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        if len(s) == 0:
            return 0
        if len(set(s)) == 1 or len(set(s)) == 2:
            return len(s)
    
        ptr1 = 0
        ptr2 = 0
        maxlen = 0
        start = 0
        for index, char in enumerate(s):
            if char == s[ptr2]:
                continue
            if char == s[ptr1]:
                ptr1, ptr2 = ptr2, index
            else:
                if index-start > maxlen:
                    maxlen = index-start
                ptr1 = ptr2
                ptr2 = index
                start = ptr1
        maxlen = max(maxlen, len(s)-start)
        
        return maxlen
        
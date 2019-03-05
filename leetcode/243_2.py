class Solution:
    def shortestDistance(self, words: 'List[str]', word1: 'str', word2: 'str') -> 'int':
        ans = float('inf')
        i1=i2=-float('inf')
        for i, word in enumerate(words):
            if word == word1:
                i1 = i
                ans = min(i1-i2,ans)
            if word == word2:
                i2 = i
                ans = min(i2-i1,ans)
        return(ans)  
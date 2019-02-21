class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        # brute-force, and it seems that it doesn't work

        # result = False
        # if not s:
        #     return True
        # if not wordDict:
        #     return False

        # for word in wordDict:
        #     loc = s.find(word)
        #     if loc != -1:
        #         # print(s[:loc])
        #         # print(s[loc+len(word):])
        #         result ^= (self.wordBreak(s[:loc], wordDict) and self.wordBreak(s[loc+len(word):], wordDict))
        #         print(result)
        #     else:
        #         temp = wordDict[:]
        #         temp.remove(word)
        #         result ^= self.wordBreak(s, temp)
        #         print(result)
        #     # if result:
        #     #     return result
        # return result
        
        # dp solution
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                # print(s[j+1:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
    
# test
if __name__ == '__main__':
    print(Solution().wordBreak('leetcode', ['leet', 'code'])) # true
    print(Solution().wordBreak('applepenapple', ['apple' , 'pen'])) # true
    print(Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])) # false
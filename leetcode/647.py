class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
            
        numchar = len(s)
        dp = [[1 for i in range(numchar)] for j in range(numchar)]
        for i in range(1, numchar):
            for j in range(numchar):
                if i+j > numchar-1:
                    break
                
                if s[j] == s[i+j]:
                    dp[j][i+j] = dp[j+1][i+j-1]
                else:
                    dp[j][i+j] = 0
        return sum([x for row in dp for x in row])-int(numchar*numchar/2-numchar/2)

# test
if __name__ == '__main__':
    print(Solution().countSubstrings("aaa"))
    print(Solution().countSubstrings('abc'))
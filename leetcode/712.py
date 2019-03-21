'''
Author: ZHAO Zinan
Created: 21. March 2019

kinds of like longest common string
''' 
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1 or not s2:
            return sum([ord(char) for char in s1]) + sum([ord(char) for char in s2])
        
        lens1 = len(s1)
        lens2 = len(s2)
        dp = [[0 for i in range(lens2+1)] for j in range(lens1+1)]

        for i in range(1, lens1+1):
            for j in range(1, lens2+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return sum([ord(char) for char in s1])+sum([ord(char) for char in s2])-2*dp[lens1][lens2]

# test
if __name__ == '__main__':
    print(Solution().minimumDeleteSum('sea', 'eat')) #231
    print(Solution().minimumDeleteSum('delete', 'leet')) # 403

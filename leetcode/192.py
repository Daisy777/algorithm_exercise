'''
Author:    ZHAO Zinan
Created: 16-May-2019

91. Decode Ways
'''
# dp
class Solution:
    def numDecodings(self, s: str) -> int:
        def valid(num):
            if len(num) == 2:
                # to determine whether the two digit string is valid letter
                if '10' <=num<= '26':
                    return 1 
                return 0 
            elif len(num) == 1:
                return int('1' <= num <= '9')


        if not s:
            return 0 

        dp = [1]*(len(s)+1)
        dp[1] = valid(s[0])

        for index in range(len(s)+1):
            if index == 0 or index == 1:
                continue 

            dp[index] = dp[index-1]*valid(s[index-1]) + dp[index-2] * valid(s[index-2:index])
        return dp[-1]


# test 
if __name__ == '__main__':
    print(Solution().numDecodings('12'))  
    print(Solution().numDecodings('226'))  
    print(Solution().numDecodings('0'))  
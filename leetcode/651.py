class Solution:
    def maxA(self, N: int) -> int:
        # # recursion consumes a lot of time when N is large
        # maxa = N
        # for i in range(N-3):
        #     maxa = max(maxa, self.maxA(i)*(N-i-1))
        # return maxa

        # dp
        dp = [i+1 for i in range(N)]
        for i in range(4, N):
            dp[i] = max(dp[i], max([dp[j]*(i-j-1) for j in range(i-3)]))
        return dp[N-1]

# test
if __name__  == '__main__':
    print(Solution().maxA(3)) # 3
    print(Solution().maxA(7)) # 9
    print(Solution().maxA(47))  # time limit
    print(Solution().maxA(5)) 
import collections 

class Solution:
    def maxUncrossedLines(self, A, B):
        dp, lena, lenb = collections.defaultdict(int), len(A), len(B)

        for i in range(lena):
            for j in range(lenb):
                dp[i, j] = max(dp[i-1, j], dp[i, j-1], dp[i-1, j-1] + int(A[i]==B[j]))
        return dp[lena-1, lenb-1]
    
if __name__ == '__main__':
    print(Solution().maxUncrossedLines([1,1,3,5,3,3,5,5,1,1], [2,3,2,1,3,5,3,2,2,1]))
            
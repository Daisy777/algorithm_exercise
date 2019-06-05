import collections

def longestCommonSubstring(A, B):
    dp, lena, lenb = collections.defaultdict(int), len(A), len(B)

    for i in range(lena):
        for j in range(lenb):
            dp[i, j] = max(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]+int(A[i] == B[j]))
    return dp[i, j]

if __name__ == '__main__':
    print(longestCommonSubstring('aaa', 'absa'))
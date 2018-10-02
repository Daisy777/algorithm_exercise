class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 1
        for i in range(1, N+1):
            res *= N//i

        return res

if __name__ == '__main__':
    print(Solution().countArrangement(7)) # 41
    

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return 0
        # find len of digits before 0
        if '0' in num:
            lenbefore0 = 0
            for digit in num:
                if digit != '0':
                    lenbefore0+=1
            if lenbefore0 <= k:
                num = num[lenbefore0:]
                k -= lenbefore0
        
        # delete the largest digits first
        for i in range(k):
            largestindex = num.index(max(num))
            num = num[:largestindex]+num[largestindex+1:]
        return num

if __name__ == '__main__':
    print(Solution().removeKdigits('10200', 1)) # 200
    print(Solution().removeKdigits('1432219', 3)) # 1219
    print(Solution().removeKdigits('10', 2)) # 0
        
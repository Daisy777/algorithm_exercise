class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(left, right+1):
            if self.selfDeviding(i):
                result.append(i)
        return result


    def selfDeviding(self, num):
        origin = num
        # print(origin)
        if num < 10 and num > 0:
            return True
        else:
            result = True

            while (result and num > 0):
                if num%10 == 0:
                    return False
                else:
                    result = (origin%(num%10)==0) and result
                    num //= 10

            return result



if __name__=='__main__':
    sol = Solution();
    print(sol.selfDividingNumbers(1, 22))
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        first = 0
        last = 0
        
        time = 0
        nearest = 0
        
        while(N > 0):
            time += 1
            if N % 2 == 1:
                if first == 0:
                    first = time
                elif last == 0:
                    last = time
                elif time - nearest > last - first:
                    first, last = nearest, time
                nearest = time
            N //= 2
        # print(last, first)
            
        return last - first if last != 0 else 0

if __name__=="__main__":
    print(Solution().binaryGap(22)) # 22 -> 0b10110
    print(Solution().binaryGap(5))  # 5 -> 0b101
    print(Solution().binaryGap(15)) # 15 -> 0b1111
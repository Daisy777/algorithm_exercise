class Solution:
    def numberOfArithmeticSlices(self, A):
        previous_diff = float('inf')
        n = 2
        total = 0
        numele = len(A)
        for i in range(1, numele):
            if A[i]-A[i-1] == previous_diff:
                n += 1
            else:
                total += int(n*n/2-3*n/2+1)
                n = 2
                previous_diff = A[i]-A[i-1]
        # print(n)
        total += int(n*n/2-3*n/2+1)
        return total
#test
if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4])) # 3
    print(Solution().numberOfArithmeticSlices([]))
    print(Solution().numberOfArithmeticSlices([5, 1,2, 3, 4]))

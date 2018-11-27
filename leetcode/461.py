class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = bin(x^y)[2:]
        return xor.count('1') 

# test
if __name__=='__main__':
    print(Solution().hammingDistance(1, 4)) # 2
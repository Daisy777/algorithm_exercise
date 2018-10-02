class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        j = len(b) - 1
        plus_one = 0
        digits = []

        while(i >= 0 and j >= 0):
            digits.append(str(int(a[i])^int(b[j])^plus_one))
            plus_one = (int(a[i]) + int(b[j]) + plus_one) // 2
            i -= 1
            j -= 1

        while(i >= 0):
            digits.append(str(int(a[i])^plus_one))
            plus_one = int(a[i]) & plus_one
            i -= 1

        while(j >= 0):
            digits.append(str(int(b[j])^plus_one))
            plus_one = int(b[j]) & plus_one
            j -= 1

        if plus_one:
            digits.append('1')

        return ''.join(list(reversed(digits)))


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_first, a_second = self.complexTwoPart(a)
        b_first, b_second = self.complexTwoPart(b)

        first = a_first*b_first - a_second*b_second
        second = a_second*b_first + a_first*b_second

        return ''.join([str(first), '+', str(second), 'i'])
        
    def complexTwoPart(self, a):
        parts = a.split('+')
        first = int(parts[0])
        second = int(parts[1].split('i')[0])

        return (first, second)


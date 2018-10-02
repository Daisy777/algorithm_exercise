class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self._plusOne(digits, len(digits))
        return digits
            
    def _plusOne(self, digits, length):
        if length == 0:
            digits.insert(0, 1)
            return 
        digits[length-1] += 1
        if digits[length-1] > 9:
            digits[length-1] = 0
            self._plusOne(digits, length-1)
            
'''
Author: ZHAO Zinan
Created: 20. February 2019

544. Output Contest Matchespyt
''' 
class Solution:
    def findContestMatch(self, n: 'int') -> 'str':
        return str(self._findContestMatch(list(range(1, n+1)))).replace(', ', ',').replace('[', '(').replace(']', ')')
    def _findContestMatch(self, arr):
        def combine(arr):
            result = []
            for i in range(len(arr)//2):
                result.append([arr[i], arr[len(arr)-1-i]])
            return result

        while (len(arr) > 2):
            arr = combine(arr)
        return arr

# test
if __name__ == '__main__':
    print(Solution().findContestMatch(2))
    print(Solution().findContestMatch(8))


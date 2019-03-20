class Solution:
    def countSubstrings(self, s: str) -> int:
        def _countSubstring(s:str, begin:int, end:int) -> int:
            if begin == 0 or end == len(s)-1:
                return 0
            
            numchar = len(str)
            dp = [[1 for i in range(numchar)] for j in range(numchar)]
            for i in range(1, numchar):
                for j in range(numchar):
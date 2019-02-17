class Solution:
    def canTransform(self, start: 'str', end: 'str') -> 'bool':
        lStart = len(start)
        lEnd = len(end)
        if lStart != lEnd:
            return False

        pStart =0
        pEnd = 0
        
        while(pStart < lStart and pEnd < lEnd):
            while pStart < lStart and start[pStart] == 'X':
                pStart += 1
            while pEnd < lEnd and end[pEnd] == 'X':
                pEnd += 1
                
            if not (pStart < lStart and pEnd < lEnd):
                break
            
            if start[pStart] != end[pEnd]:
                return False

            if start[pStart] == 'R' and pStart > pEnd:
                 return False
            if start[pStart] == 'L' and pStart < pEnd:
                 return False
            pEnd += 1
            pStart += 1

        return end.replace('X', '') == start.replace('X', '')

# test
if __name__ == '__main__':
    # False
    print(Solution().canTransform('XXRXXLXXXX', 'XXXXRXXLXX'))
    # False
    print(Solution().canTransform('X', 'L'))
    # True
    print(Solution().canTransform('RXXLRXRXL', 'XRLXXRRLX'))
    
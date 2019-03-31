class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        if not A:
            return []
        lenA = len(A)
        result = [False]*lenA
        accu = 0
        
        for index, a in enumerate(A):
            accu *= 2
            accu += a
            # print(accu)
            if accu % 5== 0:
                result[index] = True
        return result
        
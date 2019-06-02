from typing import List 

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ia, ib = 0, 0 
        intersection = []

        while (ia < len(A) and ib < len(B)):
            begina, enda, beginb, endb = A[ia][0], A[ia][1], B[ib][0], B[ib][1] 
            if beginb > enda:
                ia += 1
            elif begina > endb:
                ib += 1
            elif begina <= beginb <= enda:
                if begina <= endb <= enda:
                    intersection.append([beginb, endb])
                    ib += 1
                else:
                    intersection.append([beginb, enda]) 
                    ia += 1
            elif beginb <= begina <= endb:
                if beginb <= enda <= endb:
                    intersection.append([begina, enda]) 
                    ia += 1
                else:
                    intersection.append([begina, endb]) 
                    ib += 1
        return intersection

# test
if __name__ == '__main__':
    assert(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
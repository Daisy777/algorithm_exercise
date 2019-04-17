'''
Author: ZHAO Zinan
Created: 17. April 2019

973. K Closest Points to Origin
''' 
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not K or not points:
            return []
        points.sort(key=lambda point: point[0]**2+point[1]**2)
        return points[:K]

if __name__ == '__main__':
    print(Solution().kClosest([[-1, -1], [2, 3]], 1))
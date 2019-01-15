'''Author:    ZHAO Zinan
Created: 01/15/2019

391. Perfect Rectangle
'''
class Solution:
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if len(rectangles) == 0:
            return False
        if len(rectangles) == 1:
            return True

        expected_area = 0
        sum_area = 0
        bottom_x, bottom_y = rectangles[0][0], rectangles[0][1]
        top_x, top_y = rectangles[0][2], rectangles[0][3]
        corners = set()

        for rectangle in rectangles:
            bottom_x = min(rectangle[0], bottom_x)
            bottom_y = min(rectangle[1], bottom_y)
            top_x = max(top_x, rectangle[2])
            top_y = max(top_y, rectangle[3])

            expected_area = (top_x-bottom_x) * (top_y-bottom_y)

            sum_area += (rectangle[2]-rectangle[0]) * (rectangle[3]-rectangle[1])
            
            x1 = rectangle[0]
            x2 = rectangle[2]
            y1 = rectangle[1]
            y2 = rectangle[3]

            if (x1, y1) not in corners:
                corners.add((x1, y1))
            else:
                corners.remove((x1, y1))

            if (x1, y2) not in corners:
                corners.add((x1, y2))
            else:
                corners.remove((x1, y2))

            if (x2, y2) not in corners:
                corners.add((x2, y2))
            else:
                corners.remove((x2, y2))

            if (x2, y1) not in corners:
                corners.add((x2, y1))
            else:
                corners.remove((x2, y1))

        if (bottom_x, bottom_y) not in corners or (bottom_x, top_y) not in corners or (top_x, top_y) not in corners or (top_x, bottom_y) not in corners or len(corners) != 4:
            return False
        return sum_area == expected_area 

# test 
if __name__ == '__main__':
    # print(Solution().isRectangleCover([[0,0,1,1],[0,1,3,2],[1,0,2,2]]))
    # # False

    print(Solution().isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))
    # true

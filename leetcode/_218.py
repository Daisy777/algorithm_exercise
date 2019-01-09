class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
            
        points = []
        max_right = 0
        for index, building in enumerate(buildings):
            # first one
            if index == 0:
                points.append([building[0], building[2]])
                max_right = building[1]
                continue

            max_right = max(building[1], max_right)
            # points[len(points)-1] = [building[0], max(building[2], points[len(points)-1][1])]
                # continue

            # no overlap
            if building[0] > max_right:
                points.append([max_right, 0])
                points.append([building[0], building[2]])

            # next is lower than the previous one
            elif building[0] == buildings[index-1][0]:
                if building[2] <= buildings[index-1][2] and building[]
            #     building[2] < buildings[index-1][2]:
            #     points.append([buildings[index-1][1], building[2]])
            # # next is higher than the previous one
            # elif building[2] > buildings[index-1][2]:
            #     points.append([building[0], building[2]])

        # the last end point
        points.append([max([building[1] for building in buildings]), 0])

        return points

# test
if __name__ == '__main__':
    test0 = [ 
        [2, 9, 10], 
        [3, 7, 15],
        [5, 12, 12], 
        [15, 20, 10],
        [19, 24, 8]
    ]
    print(Solution().getSkyline(test0))
    # [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]

    test1 = [[1,2,1],[1,2,2],[1,2,3]]
    print(Solution().getSkyline(test1))
    # [[1,3],[2,0]]

    test2 = [[2,4,7],[2,4,5],[2,4,6]]
    print(Solution().getSkyline(test2))
    # [[2, 7], [4, 0]]

    test3 = [[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]
    print(Solution().getSkyline(test3))
    # [[3,8],[7,7],[8,6],[9,5],[10,4],[11,3],[12,2],[13,1],[14,0]]
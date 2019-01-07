class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        # pacific
        canaccess = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            canaccess[i][0] = 1
        for i in range(len(matrix[0])):
            canaccess[0][i] = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                canaccess[i][j] = int((canaccess[i-1][j] and matrix[i-1][j] <= matrix[i][j]) or
                                  (canaccess[i][j-1] and matrix[i][j-1] <= matrix[i][j]))
                                  
        # atlantic
        for i in range(len(matrix)-1, -1, -1):
            canaccess[i][len(matrix[0])-1] += 2
        for i in range(len(matrix[0])-1, -1, -1):
            canaccess[len(matrix)-1][i] += 2
        canaccess[len(matrix)-1][len(matrix[0])-1] -= 2
        
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])-2,-1, -1):
                if (canaccess[i+1][j] >=2 and matrix[i+1][j] <= matrix[i][j]) or (canaccess[i][j+1] >= 2 and matrix[i][j+1] <= matrix[i][j]):
                    canaccess[i][j] += 2


        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if canaccess[i][j] > 2:
                    result.append([i, j])
        return result

# test
if __name__ == '__main__':
    test0 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print(Solution().pacificAtlantic(test0))
    # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    test1 = [[1, 1], [1, 1]]
    print(Solution().pacificAtlantic(test1))
    # [[0, 0], [0, 1], [1, 0], [1, 1]]

